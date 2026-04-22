-- ═══════════════════════════════════════════════════════════
-- Supabase Vector DB 초기 설정 SQL
-- ═══════════════════════════════════════════════════════════
--
-- 사용법:
--   1. Supabase 프로젝트 생성 (https://supabase.com)
--   2. 좌측 메뉴 "SQL Editor" 클릭
--   3. 이 파일 전체를 복사해서 붙여넣기
--   4. "Run" 버튼 클릭
--
-- 연관 주차: W5 (Vector DB 기초) · W6 (Hybrid RAG)
-- ═══════════════════════════════════════════════════════════


-- ───────────────────────────────────────────────
-- 1. pgvector 확장 활성화
-- ───────────────────────────────────────────────
CREATE EXTENSION IF NOT EXISTS vector;


-- ───────────────────────────────────────────────
-- 2. documents 테이블 (메인 Vector DB)
-- ───────────────────────────────────────────────
-- 기존 테이블이 있으면 주의! 데이터 삭제됨.
-- DROP TABLE IF EXISTS documents CASCADE;

CREATE TABLE IF NOT EXISTS documents (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  content text NOT NULL,
  metadata jsonb DEFAULT '{}'::jsonb,
  embedding vector(1536),  -- OpenAI text-embedding-3-small 차원
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);


-- ───────────────────────────────────────────────
-- 3. 인덱스 (검색 성능 최적화)
-- ───────────────────────────────────────────────
-- 벡터 검색용 IVFFlat 인덱스
-- lists는 데이터 크기에 따라 조정 (10k rows → lists=100)
CREATE INDEX IF NOT EXISTS documents_embedding_idx 
  ON documents USING ivfflat (embedding vector_cosine_ops)
  WITH (lists = 100);

-- 메타데이터 필터링용
CREATE INDEX IF NOT EXISTS documents_metadata_idx 
  ON documents USING gin (metadata);

-- 시간순 조회용
CREATE INDEX IF NOT EXISTS documents_created_at_idx 
  ON documents (created_at DESC);


-- ───────────────────────────────────────────────
-- 4. 기본 유사도 검색 RPC 함수
-- ───────────────────────────────────────────────
CREATE OR REPLACE FUNCTION match_documents(
  query_embedding vector(1536),
  match_count int DEFAULT 5
) RETURNS TABLE (
  id uuid,
  content text,
  metadata jsonb,
  similarity float
) LANGUAGE plpgsql AS $$
BEGIN
  RETURN QUERY
  SELECT 
    d.id,
    d.content,
    d.metadata,
    1 - (d.embedding <=> query_embedding) AS similarity
  FROM documents d
  ORDER BY d.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;


-- ───────────────────────────────────────────────
-- 5. 메타데이터 필터링 RPC 함수 (W5 Q4)
-- ───────────────────────────────────────────────
CREATE OR REPLACE FUNCTION match_documents_filtered(
  query_embedding vector(1536),
  filter jsonb DEFAULT '{}'::jsonb,
  match_count int DEFAULT 5
) RETURNS TABLE (
  id uuid,
  content text,
  metadata jsonb,
  similarity float
) LANGUAGE plpgsql AS $$
BEGIN
  RETURN QUERY
  SELECT 
    d.id,
    d.content,
    d.metadata,
    1 - (d.embedding <=> query_embedding) AS similarity
  FROM documents d
  WHERE d.metadata @> filter  -- JSONB 포함 연산자
  ORDER BY d.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;


-- ───────────────────────────────────────────────
-- 6. 카테고리별 검색 RPC (간편 버전)
-- ───────────────────────────────────────────────
CREATE OR REPLACE FUNCTION match_documents_by_category(
  query_embedding vector(1536),
  category_name text,
  match_count int DEFAULT 5
) RETURNS TABLE (
  id uuid,
  content text,
  metadata jsonb,
  similarity float
) LANGUAGE plpgsql AS $$
BEGIN
  RETURN QUERY
  SELECT 
    d.id,
    d.content,
    d.metadata,
    1 - (d.embedding <=> query_embedding) AS similarity
  FROM documents d
  WHERE d.metadata->>'category' = category_name
  ORDER BY d.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;


-- ───────────────────────────────────────────────
-- 7. 계층적 청킹용 RPC 함수 (W6 심화)
-- ───────────────────────────────────────────────
-- child로 검색하고 parent_id 반환 → parent 본문은 별도 조회
CREATE OR REPLACE FUNCTION match_children_get_parents(
  query_embedding vector(1536),
  match_count int DEFAULT 5
) RETURNS TABLE (
  child_id uuid,
  parent_id text,
  content text,
  similarity float
) LANGUAGE plpgsql AS $$
BEGIN
  RETURN QUERY
  SELECT 
    d.id AS child_id,
    (d.metadata->>'parent_id') AS parent_id,
    d.content,
    1 - (d.embedding <=> query_embedding) AS similarity
  FROM documents d
  WHERE d.metadata->>'chunk_type' = 'child'
  ORDER BY d.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;


-- ───────────────────────────────────────────────
-- 8. 업데이트 자동 갱신 트리거
-- ───────────────────────────────────────────────
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS update_documents_updated_at ON documents;
CREATE TRIGGER update_documents_updated_at
  BEFORE UPDATE ON documents
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();


-- ───────────────────────────────────────────────
-- 9. 편의 뷰 (통계 조회)
-- ───────────────────────────────────────────────
CREATE OR REPLACE VIEW documents_stats AS
SELECT 
  COUNT(*) AS total_chunks,
  COUNT(DISTINCT metadata->>'source') AS unique_sources,
  COUNT(DISTINCT metadata->>'category') AS unique_categories,
  MIN(created_at) AS first_upload,
  MAX(created_at) AS latest_upload
FROM documents;


-- ───────────────────────────────────────────────
-- 10. 테스트 쿼리 (선택, 주석 해제 후 실행)
-- ───────────────────────────────────────────────

-- 통계 확인
-- SELECT * FROM documents_stats;

-- 샘플 데이터 삽입 (임베딩은 임시 랜덤값, 실제로는 OpenAI API 사용)
-- INSERT INTO documents (content, metadata)
-- VALUES 
--   ('FOMC가 2026년 3월 금리를 5.5%로 동결했다.', '{"category": "fomc", "source": "news.pdf", "page": 1}'),
--   ('애플이 M5 칩 탑재 MacBook Pro를 발표했다.', '{"category": "product", "source": "tech.pdf", "page": 3}');

-- 검색 테스트 (실제로는 query_embedding을 OpenAI에서 받아야 함)
-- SELECT * FROM match_documents_by_category(
--   '[0.1, 0.2, ...]'::vector(1536),  -- 실제 임베딩 벡터
--   'fomc',
--   3
-- );


-- ═══════════════════════════════════════════════════════════
-- 설치 완료! ✅
-- 
-- 다음 단계:
--   1. n8n에서 Supabase Credential 설정
--   2. SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY를 .env에 저장
--   3. W5 Q3부터 실습 시작
-- 
-- 문제 발생 시:
--   - Supabase Dashboard → Database → Tables에서 documents 테이블 확인
--   - Functions 섹션에서 match_documents 등록 확인
-- ═══════════════════════════════════════════════════════════
