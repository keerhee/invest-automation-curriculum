# 📚 참고 부록

과정 중 **수시로 참조하는 레퍼런스** 문서입니다. 막혔을 때마다 여기를 찾으세요.

## 📚 전체 목록

| 부록 | 주제 | 언제 참조? |
|:---:|---|---|
| [📘 A. n8n 매뉴얼](Appendix_A_n8n_Manual.html) | n8n 노드·표현식·에러 | **매 주차** |
| [📘 B. Hybrid RAG 가이드](Appendix_B_Hybrid_RAG_Guide.html) | RAG 튜닝·벤치마크 | W5~W7 |
| [📘 C. KIS API 레퍼런스](Appendix_C_KIS_API_Reference.html) | TR_ID·에러 코드·운영 | SP 세션 |
| [📘 D. 프롬프트 패키지](Appendix_D_Prompt_Package.html) | 16개 복붙용 프롬프트 | W3~W8 |
| [📘 E. 안전장치 체크리스트](Appendix_E_Safety_Checklist.html) | Risk Guards·사고 대응 | W8 필수 |

## 🎯 부록 활용법

### 📘 A. n8n 매뉴얼
**모든 주차에서 참조**. 노드 설정이 기억 안 날 때, 표현식 문법이 헷갈릴 때, 에러 메시지를 만났을 때.

주요 섹션:
- 12개 핵심 노드 레퍼런스 (HTTP Request · Code · Merge · IF · Switch 등)
- 표현식 치트시트 (50+ 패턴)
- 에러 Top 10 + 대응법
- 운영 팁 10가지 + FAQ 8선

### 📘 B. Hybrid RAG 가이드
**W5 이후 RAG 관련 주차에서 참조**. 청크 크기·오버랩 어떻게 정할지, Reranker를 왜 써야 하는지, 성능을 어떻게 측정할지.

주요 섹션:
- Bi-encoder vs Cross-encoder 원리
- 청킹 전략 (256~512 토큰 · 20% overlap)
- Cohere Rerank 활용
- Recall@K 측정 벤치마크
- 7가지 실패 패턴 + 해결

### 📘 C. KIS API 레퍼런스
**KIS 특별세션 + 한국 주식 연동 시 참조**. TR_ID 전체 맵·에러 코드 20선·운영 패턴 5가지.

주요 섹션:
- OAuth + HashKey 완벽 가이드
- 국내주식 시세/주문/잔고 API 15개+
- TR_ID 모의/실전 대조표
- EGW00121 등 에러 코드 20선
- Rate Limit + 운영 패턴

### 📘 D. 프롬프트 패키지
**Claude 프롬프트 작성할 때 복사·붙여넣기**. 16개 검증된 프롬프트 + 복사 버튼 지원.

포함된 프롬프트:
- W3: 뉴스 센티먼트 분석 + 다중 뉴스 종합
- W4: 차트 Vision 판독 + 3D Verdict
- W5: 시장별 모닝 브리핑
- W6: RAG 출처 인용 Q&A
- W7: Orchestrator + Sub-agents
- W8: 주문 결정 + KIS 한국 주식
- 공통: 5가지 튜닝 패턴

### 📘 E. 안전장치 체크리스트
**W8 실습 + 실전 전환 검토 시 필독**. 사고 예방의 핵심 문서.

주요 섹션:
- Risk Guards 4단계 (Position · Stop · Profit · Daily Loss)
- 2단계 승인 시스템
- 로깅 3단계 구조
- 실계좌 전환 7대 검증
- 사고 대응 프로토콜 (10분 골든타임)

## 🔍 빠른 검색 팁

### 브라우저 내 검색
모든 부록은 한 페이지 HTML이므로 `Ctrl+F` (Mac: `Cmd+F`)로 바로 검색 가능.

예시 검색 키워드:
- "EGW00121" → 부록 C에서 즉시 찾음
- "chunk size" → 부록 B
- "Position Sizing" → 부록 E
- "Rate Limit" → 부록 A + C

### 사이드바 내비게이션
각 부록은 고정 TOC가 있어 섹션 간 이동이 쉽습니다.

## 📌 인쇄용 사용

장기 참조 용도로 종이에 인쇄할 경우:
- 브라우저에서 `Ctrl+P` (Mac: `Cmd+P`)
- "배경 그래픽" 옵션 켜기 (색상 유지)
- "여백: 좁게"로 설정하면 페이지 수 절약

---

[← docs/](../README.md) · [📖 강의노트](../lectures/README.md) · [💻 실습](../labs/README.md) · [📝 과제](../homework/README.md)
