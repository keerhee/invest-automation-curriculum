# 🛠️ 재사용 템플릿

과정 중 바로 복사해서 쓸 수 있는 템플릿 모음입니다.

## 📂 구조

```
templates/
├── env/              # 환경변수 템플릿
│   └── .env.example
├── n8n/              # n8n 워크플로 JSON
│   ├── W1_Sample_Price_Collector.json
│   └── W5_Sample_Error_Handler.json
└── supabase/         # Vector DB 스키마
    └── init_schema.sql
```

## 🔐 env/

**용도**: API 키·설정 관리  
**사용법**:
```bash
cp templates/env/.env.example .env
# 그리고 .env 파일을 열어 각 값 교체
```

⚠️ `.env` 파일은 절대 커밋하지 마세요. `.gitignore`에 이미 포함되어 있습니다.

## ⚙️ n8n/

**용도**: 검증된 워크플로를 import해서 바로 사용  
**사용법**:
```
1. n8n 에디터에서 우측 상단 "..." → "Import from File"
2. templates/n8n/*.json 선택
3. Credential 재설정 (Discord, API 키 등)
4. 본인 상황에 맞게 수정
```

### 포함된 샘플

- **W1_Sample_Price_Collector** — 가장 기본적인 4-노드 구조 (Manual → HTTP → Code → Discord)
- **W5_Sample_Error_Handler** — Error Trigger + Rate Limit 재시도 + 알림

### 주의

- Credential ID는 본인의 것으로 교체 필수
- 샘플은 **학습용 출발점**이지 완성품이 아님
- Import 후 실제로 테스트 실행해서 동작 확인

## 🗄️ supabase/

**용도**: Supabase 프로젝트 초기 설정  
**사용법**:
```
1. Supabase Dashboard → SQL Editor
2. templates/supabase/init_schema.sql 전체 복사
3. 붙여넣고 "Run" 클릭
4. Tables 섹션에서 documents 테이블 확인
5. Functions 섹션에서 match_documents 등 확인
```

### 포함된 것

- pgvector 확장 활성화
- documents 테이블 (1536차원 embedding)
- 3개 RPC 함수 (기본 검색 · 메타데이터 필터 · 카테고리 필터)
- 계층적 청킹용 함수 (W6 심화)
- 업데이트 트리거
- 통계 뷰

## 💡 커스터마이징

자신의 환경에 맞게 수정한 템플릿을 다른 수강생들과 공유하고 싶다면:

1. [CONTRIBUTING.md](../CONTRIBUTING.md) 참조
2. 포크 → 수정 → Pull Request
3. `templates/` 폴더에 새 파일 추가

---

[← 리포 메인](../README.md)
