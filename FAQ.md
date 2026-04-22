# ❓ 자주 묻는 질문 (FAQ)

커리큘럼 진행 중 가장 많이 받는 질문들입니다. **Ctrl+F** 로 키워드 검색을 활용하세요.

---

## 📋 목차

1. [💭 입문 전 고민](#-입문-전-고민)
2. [🛠️ 환경 설정](#️-환경-설정)
3. [💰 비용 관련](#-비용-관련)
4. [🐛 에러 해결](#-에러-해결)
5. [📝 과제 관련](#-과제-관련)
6. [🎓 수료 후 진로](#-수료-후-진로)
7. [⚠️ 실전 관련](#️-실전-관련)

---

## 💭 입문 전 고민

### Q1. 프로그래밍 경험이 전혀 없는데 가능한가요?

**가능합니다.** n8n이 드래그앤드롭 방식이라 초반은 코드 없이도 진행할 수 있습니다. Python은 W1~W4에서는 간단한 문법만, W5 이후로 점진적으로 늘어납니다. 막히면 Claude에게 질문하면 대부분 해결됩니다.

### Q2. 수학·통계 지식이 필요한가요?

- **고등학교 수학** 수준이면 충분합니다 (평균, 표준편차)
- RSI·볼린저밴드 같은 지표 수식은 모두 설명이 포함되어 있습니다
- W6의 RAG 관련 내용도 "벡터 유사도"를 직관적으로만 이해하면 됩니다

### Q3. 금융 지식이 없어도 되나요?

**네.** W1부터 기초 개념을 설명합니다. 다만 "주가", "거래량", "지수"가 뭔지 정도는 아시는 게 좋습니다. 모른다면 네이버 금융 메인 화면 10분 살펴보는 것으로 충분합니다.

### Q4. Mac이어야 하나요? Windows·Linux 가능한가요?

**모두 가능합니다.** 실습은 대부분 브라우저와 Python으로 이루어지며 OS 의존성은 거의 없습니다.

### Q5. 노트북 사양은 어느 정도가 필요한가요?

일반 사무용 노트북이면 충분합니다:
- RAM 8GB 이상
- 저장공간 5GB 여유
- 인터넷 연결

GPU, 고성능 CPU 불필요. n8n Cloud를 쓰면 로컬 부담도 없습니다.

---

## 🛠️ 환경 설정

### Q6. n8n Cloud vs Self-hosted 어떤 걸 써야 하나요?

**초보자는 n8n Cloud 추천**:
- 설치 불필요 (회원가입만)
- 14일 무료 체험 가능
- 강의 진행에 최적화

**Self-hosted (Docker)가 적합한 경우**:
- 클라우드 비용 장기적으로 부담
- 데이터를 외부 서버에 두기 싫음
- Docker 경험이 있음

```bash
# Self-hosted 한 줄 설치
docker run -it --rm -p 5678:5678 -v ~/.n8n:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

### Q7. Python은 어떤 버전이 필요한가요?

**Python 3.10 이상** 권장. Anaconda 또는 [python.org](https://python.org) 공식 다운로드.

```bash
# 버전 확인
python --version   # Python 3.10.x 이상이면 OK

# 가상환경 만들기 (프로젝트별 격리)
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 필요 라이브러리 설치
pip install anthropic openai pandas yfinance requests
```

### Q8. Jupyter Notebook을 처음 써봐요.

**Google Colab으로 시작**: 설치 불필요, 브라우저만 있으면 됨.
```
https://colab.research.google.com
```
.ipynb 파일을 직접 업로드해서 실행 가능.

**로컬 설치**:
```bash
pip install jupyter
jupyter notebook
# 브라우저가 열리면 .ipynb 파일 열기
```

### Q9. `.env` 파일은 어디에 둬야 하나요?

**프로젝트 루트 디렉토리**에 둡니다.

```
your-project/
├── .env                # 여기!
├── .gitignore          # .env가 포함되어 있어야 함
├── docs/
└── ...
```

**절대 커밋하지 마세요**. `.gitignore`에 `.env`가 있는지 반드시 확인.

### Q10. Google Sheets 연동이 안 돼요.

가장 흔한 원인:
1. **OAuth 인증 안 됨** - n8n Credentials에서 Google Sheets 클릭 → "Sign in with Google" 필요
2. **스프레드시트 권한 없음** - 파일을 열고 공유 설정 확인
3. **시트 이름 오타** - 대소문자 정확히
4. **Document ID 잘못** - URL의 `/d/` 다음 긴 문자열이 ID

---

## 💰 비용 관련

### Q11. 과정 전체 비용이 얼마나 드나요?

대부분의 무료 크레딧을 활용하면 **$10~20** 수준:

| 항목 | 예상 비용 |
|---|---|
| Anthropic (Claude) | $3~5 (초기 $5 크레딧 활용 후) |
| OpenAI (Embeddings) | $1~3 |
| n8n Cloud | $0 (14일 무료) 또는 $20 |
| Cohere | $0 (Trial 무료 1000회) |
| Supabase | $0 (Free tier) |
| **합계** | **$4~28** |

### Q12. 유료 결제 꼭 해야 하나요?

Anthropic은 **결제카드 등록이 필수**입니다 (사용량 기반). 다만:
- 월 $5 이하로 제한 설정 가능
- 학생 크레딧 신청 가능 (학교 이메일)
- 과제마다 월 $1도 안 쓰는 수준

### Q13. 비용이 폭발할까 봐 걱정이에요.

**안전장치 3개**:
1. **모델 선택**: Haiku 사용 (Sonnet의 1/3 비용)
2. **Console Alert**: $5 초과 시 이메일 알림 설정
3. **Monthly Cap**: Anthropic Console에서 월 최대 한도 설정

Claude Opus는 교과 과정에서 거의 사용하지 않습니다 (너무 비쌈).

### Q14. 실수로 비용이 많이 나왔어요.

1. **즉시 키 비활성화** (Anthropic Console)
2. **원인 분석**: 어떤 워크플로가 비용 폭증?
3. **Anthropic 고객지원** 연락 (초보자 실수는 일부 환불 가능)
4. 다음부터는 **Rate Limit + Max Tokens** 설정 철저히

---

## 🐛 에러 해결

### Q15. n8n에서 `Request failed with status code 429`

**Rate Limit 초과**. API 제공자가 너무 많은 요청을 거부한 것.

해결:
- Wait 노드 추가 (2~5초)
- CoinGecko: 분당 30회 제한 → Wait 2초
- Alpha Vantage: 분당 5회 → Wait 15초
- KIS 모의: 초당 2 TPS → Wait 0.6초

### Q16. `EGW00121` (KIS) 에러가 나요.

**HashKey 불일치**. 부록 C의 HashKey 섹션 참고. 핵심:
- 주문 Body와 HashKey 생성 Body가 **완전히 동일**해야 함
- Set 노드에서 Body를 한 번만 만들고 재사용
- JSON 순서·공백까지 동일

### Q17. `Cannot read properties of undefined`

**옵셔널 체이닝 사용**:
```javascript
// ❌ 에러 발생
const price = $json.data.price;

// ✅ 안전
const price = $json?.data?.price ?? 0;
```

### Q18. Claude가 JSON 대신 `\`\`\`json...\`\`\``로 감싸서 반환해요.

**후처리**:
```javascript
const raw = $json.content[0].text;
const clean = raw.replace(/```json\n?|```/g, '').trim();
const parsed = JSON.parse(clean);
```

또는 프롬프트에 "JSON만 출력. 마크다운 코드블록 금지" 추가.

### Q19. Vector Store 검색 결과가 엉뚱해요.

흔한 원인:
1. **청크 크기**: 너무 크면 (>2000자) 의미 희석 → 500~1000자로 축소
2. **임베딩 모델 불일치**: 저장 시와 검색 시 다른 모델
3. **데이터 부족**: 10건 미만이면 검색 의미 없음
4. **메타데이터 오타**: category 필터가 안 맞음

### Q20. Discord 웹훅이 작동 안 해요.

체크리스트:
- Webhook URL이 정확한지 (복사 실수)
- 채널 삭제되지 않았는지
- 메시지 길이 2000자 초과했는지
- 봇 권한 Role이 낮은지

---

## 📝 과제 관련

### Q21. 과제 제출은 어떻게 하나요?

각 워크북 하단의 "제출 가이드" 섹션 참조. 일반적으로:
- Discord `#homework-wN` 채널에 zip 업로드
- 또는 GitHub submissions/ 폴더에 PR
- 강사 지시에 따라 다를 수 있음

### Q22. 심화 과제(Q4, Q5)는 꼭 해야 하나요?

**필수 아님**. Q1~Q3만 만점(70점)이어도 통과(60점 이상)입니다.

다만:
- 포트폴리오로 쓰려면 심화까지 하는 게 유리
- Q4~Q5가 다음 주차의 기초가 되는 경우가 많음

### Q23. 과제가 너무 어려워요.

순서대로 시도:
1. **힌트 블록 펼쳐보기** (과제 카드 안)
2. **공식 문서 읽기** (부록 A, C 참조)
3. **Claude에게 질문** (막힌 지점 구체적으로)
4. **Discord `#question` 채널**
5. **TA 세션 참여** (매주 금요일 저녁)

아무리 막혀도 **24시간 이상 혼자 고민하지 마세요**. 질문은 부끄러운 게 아닙니다.

### Q24. 다른 사람 과제를 참고해도 되나요?

**구조·아이디어는 참고 가능**, **코드 복붙은 표절**.

괜찮은 경우:
- "저는 Switch 노드로 분기했는데 IF 노드로도 되나요?" 같은 구조 논의
- 막혔을 때 방향 제시 요청

안 되는 경우:
- 워크플로 JSON 통째로 복사
- 다른 사람 이름만 지우고 제출

### Q25. 과제 채점 불만이 있어요.

1. **루브릭 재확인**: 채점 기준이 명시되어 있습니다
2. **강사에게 문의**: 구체적인 감점 사유 질문
3. **재제출 기회**: 강사 재량에 따라 가능

---

## 🎓 수료 후 진로

### Q26. 이 과정 수료하면 어떤 직무로 갈 수 있나요?

**직접 연관**:
- **퀀트 개발자** (초급): 자동매매 시스템 엔지니어
- **데이터 엔지니어**: 금융 데이터 파이프라인
- **AI 엔지니어**: LLM 애플리케이션 개발

**간접 연관**:
- **증권/핀테크 IT**: 백엔드·프론트엔드
- **CFA/AICPA 공부 병행**: 금융 지식 플러스
- **개인 스타트업**: AI SaaS · 핀테크 앱

### Q27. 이걸로 취업 준비하려면 뭘 더 해야 하나요?

추천 심화 학습:
1. **CS 기초**: 자료구조·알고리즘 (코딩 테스트용)
2. **금융 지식**: CFA Level 1 교재, 증권분석사
3. **백엔드**: Spring Boot 또는 FastAPI
4. **데이터베이스**: SQL, PostgreSQL 심화
5. **포트폴리오**: 본 커리큘럼 결과물 + 2~3개 추가 프로젝트

### Q28. 대학원 진학에 도움이 되나요?

금융공학·퀀트 관련 대학원 지원 시 **실전 프로젝트 경험**으로 가치 있습니다. 특히:
- W7의 멀티 에이전트 오케스트레이션
- W6의 RAG 평가 (Recall@K 측정)
- 본인만의 수료 프로젝트

GPA + 추천서 + 포트폴리오 삼박자 중 하나로.

### Q29. 본 과정만으로 실전 트레이더가 될 수 있나요?

**안 됩니다.** 이 과정은 **엔지니어링 교육**이지 투자 수익 창출 가이드가 아닙니다.

실전 트레이더가 되려면 추가로 필요한 것:
- 최소 1~2년 Paper Trading 경험
- 금융 이론 깊이 있는 학습
- 리스크 관리 전문성
- 심리적 통제력
- 자본력

본 과정은 그 길의 **첫걸음**입니다.

---

## ⚠️ 실전 관련

### Q30. 실계좌로 언제 전환하면 되나요?

**권장하지 않습니다.** [`SAFETY.md`](SAFETY.md)의 "실계좌 전환 7대 검증" 참조.

혹시 전환한다면 최소:
- 3개월 이상 Paper 무중단 운영
- Sharpe Ratio 1.0+
- Max Drawdown -10% 이내
- 잃어도 되는 금액으로 시작 (총자산의 1~2%)

### Q31. 자동매매로 돈을 벌 수 있나요?

**확률적으로 대부분 손실 봅니다.** 개인 알고리즘 트레이더의 80~90%가 장기적으로 손실. 이유:
- 정보·자본·속도 면에서 기관 투자자에 열세
- 수수료·세금 누적 효과
- 심리적 실수 (자동화도 설계자가 인간)
- 백테스트 과적합

**"쉽게 돈 버는 방법"이 아니라 "안전하게 학습하는 도구"**로 접근하세요.

### Q32. 본 과정에서 제공하는 시스템을 그대로 실전에 쓰면 되나요?

**절대 안 됩니다.**

이유:
- 교육용으로 **단순화된 로직**
- 시장 변화에 대응하는 고도의 파라미터 튜닝 없음
- 실전 수준의 **리스크 관리 부족**
- 세금·수수료 계산 미포함
- 수수백만원 단위 자본에 적합한 구조 아님

과정 코드는 **학습 출발점**이지 **완제품이 아닙니다**.

---

## 📚 더 많은 자료

- [README.md](README.md) - 기본 안내
- [SAFETY.md](SAFETY.md) - 안전 수칙
- [CONTRIBUTING.md](CONTRIBUTING.md) - 기여 방법
- [CHANGELOG.md](CHANGELOG.md) - 변경 이력
- [부록 A: n8n 매뉴얼](docs/appendix/Appendix_A_n8n_Manual.html)
- [부록 C: KIS API 레퍼런스](docs/appendix/Appendix_C_KIS_API_Reference.html)
- [부록 E: 안전장치 체크리스트](docs/appendix/Appendix_E_Safety_Checklist.html)

---

## 💬 여기에 없는 질문이 있다면

1. [GitHub Discussions](https://github.com/YOUR_ORG/invest-automation-curriculum/discussions) 검색
2. Discord `#question` 채널
3. 새로운 [Issue](https://github.com/YOUR_ORG/invest-automation-curriculum/issues/new/choose) 열기

**자주 묻는 질문으로 추가되면 이 문서에 반영합니다.**
