<div align="center">

# 🤖 투자 자동화 커리큘럼

**AI 에이전트 · n8n · 페이퍼 트레이딩으로 배우는 8주 실습형 교육 과정**

![Week](https://img.shields.io/badge/curriculum-8_weeks-blue)
![Level](https://img.shields.io/badge/level-beginner_to_intermediate-green)
![License](https://img.shields.io/badge/license-CC_BY--NC_4.0-orange)
![Update](https://img.shields.io/badge/last_update-2026--04-informational)

[📚 커리큘럼 개요](#-커리큘럼-한눈에) · [🚀 빠른 시작](#-빠른-시작) · [📖 자료 구조](#-자료-구조) · [🛠️ 환경 준비](#️-환경-준비) · [❓ FAQ](#-faq)

### 🌐 [온라인으로 바로 열람하기 →](https://keerhee.github.io/invest-automation-curriculum/)

강의 노트 · 과제 · 부록을 브라우저에서 바로 확인하세요. (다운로드 불필요)

</div>

---

## 📖 이 리포가 무엇인가?

수강생이 **n8n + Claude + 금융 API**를 활용해 **자기만의 자동 매매 리서치 시스템**을 직접 구축하는 8주 과정 전체 자료입니다.

단순히 라이브러리 사용법이 아니라:

- 📊 **3차원 분석** — 가격(Price) · 뉴스(News) · 차트(Chart)를 AI로 통합 판단
- 🤖 **멀티 에이전트** — 전문 분야별 에이전트 팀을 Orchestrator로 조율
- 🛡️ **Risk Guards** — 실전 수준의 4단계 안전장치
- 📈 **Paper Trading** — Alpaca + KIS 모의투자로 실 주문 파이프라인까지

완주 시 수강생은 "AI 분석 → 판단 → 승인 → 실제 주문" 전 과정을 자신의 손으로 구축한 경험을 얻습니다.

> ⚠️ **교육 목적 선언**: 본 자료는 학습 목적이며 투자 권유가 아닙니다. 모든 실습은 Paper Trading(가상 자본)으로 진행하며, 실계좌 전환은 수강생 본인 책임입니다. 자세한 내용은 [`SAFETY.md`](SAFETY.md) 참조.

---

## 📚 커리큘럼 한눈에

| 주차 | 주제 | 핵심 기술 | 과제 |
|:---:|---|---|:---:|
| **W1** | 데이터 수집 자동화 | CoinGecko · Yahoo Finance · FRED · Google Sheets | 🟢 5 |
| **W2** | 기술적 지표 계산 | RSI · MA · 볼린저 밴드 · MACD · 수식 직접 구현 | 🟢 5 |
| **W3** | 뉴스 센티먼트 분석 | Alpha Vantage · Claude Haiku · 2차원 분석 | 🟢 5 |
| **W4** | 차트 Vision + 3D Verdict | Chart-IMG · Claude Vision · AI Agent | 🟢 5 |
| **W5** | 스케줄링 + Vector DB 기초 | Supabase pgvector · 첫 RAG · 멀티 스케줄 | 🟢 5 |
| **W6** | Hybrid RAG 실전 | PDF 임베딩 · Cohere Rerank · 출처 인용 Q&A | 🟢 5 |
| **W7** | 멀티 에이전트 | Orchestrator + 3 Sub-Agents · Message Bus | 🟢 5 |
| **W8** | Paper Trading + 수료 | Alpaca · Risk Guards · Bracket Order · 발표 | 🟢 5 |
| **SP** | KIS 모의투자 | OAuth · HashKey · 한국 주식 · 호가 단위 | 🟢 5 |

**총 45개 과제 · 9개 주차 · 예상 학습 시간 60~70시간**

전체 커리큘럼 개요는 [`docs/lectures/00_Curriculum_Overview.html`](docs/lectures/00_Curriculum_Overview.html) 참조.

---

## 🚀 빠른 시작

### 수강생용 (처음 시작하는 경우)

```bash
# 1. 리포 클론
git clone https://github.com/YOUR_ORG/invest-automation-curriculum.git
cd invest-automation-curriculum

# 2. 브라우저로 전체 개요 먼저 열기
open docs/lectures/00_Curriculum_Overview.html
# (Windows) start docs\lectures\00_Curriculum_Overview.html
# (Linux)   xdg-open docs/lectures/00_Curriculum_Overview.html

# 3. W1 강의노트 + 실습 + 과제 순서로 진행
open docs/lectures/W1_Lecture_Notes.html         # ① 강의노트 읽기
jupyter notebook docs/labs/W1_Lab.ipynb          # ② 실습 코드 돌려보기
open docs/homework/W1_Homework.html              # ③ 과제 확인

# 4. 환경변수 파일 준비 (첫 주차에 필요)
cp templates/env/.env.example .env
# .env 파일을 열고 각 API 키 입력
```

### 강사/TA용 (수업 준비)

```bash
# 1. 리포 포크 후 자기 수업용 브랜치 생성
git checkout -b my-class-2026-spring

# 2. 강의별 수업 자료 준비
#    - lectures/ 안의 HTML을 프로젝터에서 직접 띄우거나
#    - 강의 자료 PPT가 있다면 별도 제작 (roadmap에 포함)

# 3. 수강생 과제 수합용 구조 생성
mkdir -p submissions/{W1,W2,W3,W4,W5,W6,W7,W8,SP}
echo "submissions/" >> .gitignore  # 수강생 제출물은 커밋하지 않음
```

---

## 📂 자료 구조

```
invest-automation-curriculum/
│
├── 📖 README.md                    # 여기부터 시작
├── 🛡️ SAFETY.md                    # 안전 수칙 (필독)
├── 📜 LICENSE                      # CC BY-NC 4.0
├── 🤝 CONTRIBUTING.md              # 기여 가이드 (강사/수강생)
├── 💬 CODE_OF_CONDUCT.md           # 커뮤니티 규범
├── ❓ FAQ.md                       # 자주 묻는 질문
├── 📝 CHANGELOG.md                 # 버전 변경 이력
│
├── docs/                           # 📚 학습 자료 전체
│   ├── lectures/                   #   ├ 강의노트 HTML 10개
│   │   ├── 00_Curriculum_Overview.html
│   │   ├── W1_Lecture_Notes.html ~ W8_Lecture_Notes.html
│   │   └── SP_KIS_API_Special_Sessions.html
│   │
│   ├── labs/                       #   ├ Jupyter 실습 8개
│   │   ├── W1_Lab_Price_Collection.ipynb
│   │   └── ... W8_Lab_Paper_Trading.ipynb
│   │
│   ├── homework/                   #   ├ 과제 워크북 9개
│   │   ├── W1_Homework.html ~ W8_Homework.html
│   │   └── KIS_Homework.html
│   │
│   └── appendix/                   #   └ 참고 문서 부록 5개
│       ├── Appendix_A_n8n_Manual.html
│       ├── Appendix_B_Hybrid_RAG_Guide.html
│       ├── Appendix_C_KIS_API_Reference.html
│       ├── Appendix_D_Prompt_Package.html
│       └── Appendix_E_Safety_Checklist.html
│
├── templates/                      # 🛠️ 재사용 템플릿
│   ├── n8n/                        #   ├ n8n 워크플로 예시 JSON
│   ├── supabase/                   #   ├ Vector DB 스키마 SQL
│   └── env/                        #   └ .env 예시 파일
│
├── scripts/                        # 🔧 유틸리티 스크립트
│   ├── verify_env.py               #   └ 환경변수 검증
│   └── generate_submission.py      #     과제 제출 폴더 생성
│
└── .github/                        # 🐙 GitHub 설정
    ├── ISSUE_TEMPLATE/             #   ├ 질문·버그 리포트 템플릿
    └── workflows/                  #   └ 링크 검증 자동화
```

---

## 🛠️ 환경 준비

### 필수 준비물

| 도구 | 용도 | 비용 |
|---|---|---|
| **n8n Cloud** 또는 Self-hosted | 워크플로 자동화 | Cloud 무료 14일 / Self-hosted 무료 |
| **Anthropic API** | Claude 호출 | $5 크레딧 제공 · 과정 전체 $3~10 예상 |
| **OpenAI API** | Embeddings | $5 크레딧 · 과정 전체 $1~3 |
| **Cohere API** | Reranker | Trial 1000회 무료 |
| **Supabase** | Vector DB | Free tier (500MB) |
| **Alpaca** | Paper Trading | 완전 무료 |
| **KIS Developers** | 한국 주식 모의 | 완전 무료 |
| **Google Sheets** | 데이터 로깅 | 무료 |
| **Discord** | 알림 채널 | 무료 |

### API 키 발급 순서 (W1 시작 전)

```
1. Anthropic    → https://console.anthropic.com (결제 카드 필수)
2. OpenAI       → https://platform.openai.com
3. FRED         → https://fred.stlouisfed.org/docs/api/api_key.html
4. Alpha Vantage → https://www.alphavantage.co/support/#api-key
5. Cohere       → https://dashboard.cohere.com/api-keys (W6에서 필요)
6. Supabase     → https://supabase.com (W5에서 프로젝트 생성)
7. Alpaca       → https://alpaca.markets (W8에서 Paper 계정)
8. KIS          → https://apiportal.koreainvestment.com (SP에서 신청)
```

`.env` 파일 템플릿은 [`templates/env/.env.example`](templates/env/.env.example) 참조.

### 환경 검증

```bash
# 모든 환경변수가 정상 설정됐는지 자동 확인
python scripts/verify_env.py
```

---

## 📝 과제 제출 가이드

수강생은 각 주차마다 과제 워크북의 **5개 과제**(필수 3 + 심화 2) 중 최소 필수 3개를 완료해야 합니다.

### 제출 폴더 자동 생성

```bash
# W1 과제 폴더 템플릿 생성
python scripts/generate_submission.py --week W1 --name HongGilDong

# 생성되는 구조:
# submissions/W1_HongGilDong/
#   ├── Q1_BTC_Price.json
#   ├── Q2_Triple_API.json
#   ├── Q3_Schedule.json
#   ├── Q4_MultiStock.json (심화)
#   ├── Q5_Alert.json (심화)
#   ├── screenshots/
#   └── README.md
```

### 채점 기준 (각 주차 100점 만점)

- **Q1~Q3 (필수)**: 70점 · 모두 제출해야 과정 통과
- **Q4~Q5 (심화)**: 30점 · 추가 점수
- **통과선**: 60점 이상

---

## 🤝 커뮤니티

- **💬 Discord**: 질문·토론·과제 공유 (초청 링크는 수업 첫날 배포)
- **🐛 이슈**: 버그·오류·개선 제안 → [GitHub Issues](https://github.com/YOUR_ORG/invest-automation-curriculum/issues)
- **🎓 TA 세션**: 매주 금요일 저녁 2시간 실시간 Q&A (수업 주차 중)

---

## ❓ FAQ

### Q. 프로그래밍 경험이 없어도 가능한가요?

네. W1~W2는 Python 기초만 알면 됩니다. n8n이 드래그앤드롭 방식이라 오히려 코드 작성 부담이 적습니다. W6 이후는 조금 복잡해지지만 샘플 코드가 제공됩니다.

### Q. 비용이 얼마나 드나요?

과정 전체에서 API 비용은 **$10~20** 수준입니다. Anthropic과 OpenAI의 무료 크레딧($5씩)으로 대부분 커버됩니다. 거래는 Paper Trading이라 0원.

### Q. 실전 계좌에서 쓸 수 있나요?

**절대 권장하지 않습니다**. 8주 학습으로 실전 사용은 위험합니다. 자세한 내용은 [`SAFETY.md`](SAFETY.md)의 "실계좌 전환 7대 검증" 참조. 본 과정은 **AI/엔지니어링 교육**이 주목적이지 수익 창출 도구가 아닙니다.

### Q. 더 많은 질문이 있습니다.

[`FAQ.md`](FAQ.md)에 50+ 개 질문과 답변이 있습니다.

---

## 📜 라이선스

**Creative Commons BY-NC 4.0**

✅ **허용**:
- 학습 · 복습 · 개인 프로젝트
- 비영리 교육 기관에서의 수업 사용
- 포크 · 수정 · 재배포 (출처 표기)

❌ **금지**:
- 상업적 목적 (유료 강의·컨설팅에 무단 사용)
- 출처 미표기 재배포

인용 시:
```
투자 자동화 커리큘럼 (2026)
https://github.com/YOUR_ORG/invest-automation-curriculum
CC BY-NC 4.0
```

---

## 🙏 감사의 말

이 커리큘럼은 **ZeroOneAI** 교육 브랜드에서 설계·제작되었습니다. 수많은 오픈소스 라이브러리와 공개 문서가 없었다면 불가능했을 것입니다:

- [n8n.io](https://n8n.io) - 워크플로 자동화 플랫폼
- [Anthropic](https://anthropic.com) - Claude AI
- [Alpaca](https://alpaca.markets) - Paper Trading API
- [한국투자증권 Open API](https://apiportal.koreainvestment.com)
- 그리고 모든 피드백을 주신 베타 수강생 여러분

---

<div align="center">

**🎓 시작할 준비가 되셨나요?**

[📖 W1 강의노트 시작하기](docs/lectures/W1_Lecture_Notes.html) →

</div>
