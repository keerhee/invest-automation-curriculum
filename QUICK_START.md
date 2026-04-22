# 🚀 QUICK START - 5분 안에 시작하기

이 문서를 **딱 5분만** 읽으시면 커리큘럼을 시작할 준비가 끝납니다.

---

## 1️⃣ 지금 당장 할 일 (1분)

### 리포 압축 해제

```bash
unzip invest-automation-curriculum.zip
cd invest-automation-curriculum
```

### 첫 문서 열기

```bash
# macOS
open README.md

# Windows
start README.md

# Linux
xdg-open README.md
```

또는 VS Code로 폴더 자체를 열면 전체 파일을 쉽게 둘러볼 수 있습니다:

```bash
code invest-automation-curriculum
```

---

## 2️⃣ 무엇부터 읽을까? (2분)

**이 순서대로** 딱 3개 문서만 먼저:

| # | 파일 | 시간 | 왜? |
|:---:|---|:---:|---|
| 1 | `README.md` | 5분 | 전체 개요·구조 파악 |
| 2 | `SAFETY.md` | 5분 | **필수** · 안전 수칙 |
| 3 | `docs/lectures/00_Curriculum_Overview.html` | 15분 | 커리큘럼 전체 그림 |

**3개만 읽으면 "뭐부터 해야 하지?"가 없어집니다.**

---

## 3️⃣ API 키 발급하기 (첫 주에만 필요한 것들, 30분)

**W1 시작 전에 이 3개만 발급**하면 됩니다:

### Step 1: Anthropic API Key (필수)

```
https://console.anthropic.com/settings/keys
→ "Create Key" → 이름 입력 → 발급 → 안전한 곳에 저장
```

결제 카드 등록 필요 (월 $5 한도 설정 권장).

### Step 2: FRED API Key (무료)

```
https://fred.stlouisfed.org/docs/api/api_key.html
→ "Request API Key" → 이메일만 입력 → 즉시 발급
```

### Step 3: Discord Webhook

```
Discord 본인 서버 또는 개인 서버
→ 채널 우측 톱니바퀴 → 연동 → 웹후크 → URL 복사
```

### 나머지 키는 나중에

W3, W5, W6, W8, SP 시작할 때 필요한 키만 그때 발급하세요. 한 번에 다 받을 필요 없습니다.

---

## 4️⃣ .env 파일 만들기 (2분)

### 템플릿 복사

```bash
cp templates/env/.env.example .env
```

### 열어서 수정

```bash
# macOS
open .env

# 또는 원하는 에디터로
nano .env
code .env
```

### 위에서 받은 3개 키 입력

```bash
ANTHROPIC_API_KEY=sk-ant-api03-진짜_키_입력
FRED_API_KEY=진짜_키_입력
DISCORD_WEBHOOK_GENERAL=https://discord.com/api/webhooks/진짜_URL
```

### 저장하고 검증

```bash
python scripts/verify_env.py --week W1
```

**모든 체크가 초록색 ✓가 나오면 준비 완료!**

---

## 5️⃣ W1 시작! (여기부터는 당신의 여정)

### 학습 순서 (매 주차 공통)

```
① 강의노트 읽기 (60~90분)
   docs/lectures/W1_Lecture_Notes.html

② Python 실습 돌려보기 (60~120분)
   docs/labs/W1_Lab.ipynb
   (Jupyter 또는 Google Colab)

③ 과제 완료 (3~5시간)
   docs/homework/W1_Homework.html

④ 과제 제출 폴더 자동 생성
   python scripts/generate_submission.py --week W1 --name YourName

⑤ Discord에 제출
```

---

## 🆘 막혔을 때

### 자주 묻는 질문 먼저

```bash
open FAQ.md   # 50+개 질문과 답변
```

### n8n 관련 모든 것

```bash
open docs/appendix/Appendix_A_n8n_Manual.html
```

### Discord 커뮤니티

```
#question 채널에 구체적으로 질문
→ 24시간 내 TA 또는 동료 답변
```

### 비상 연락

매주 **금요일 저녁 TA 세션** · 실시간 Q&A 2시간

---

## 📚 이 리포 안에 뭐가 있나?

핵심만 요약:

- **9개 주차** × **5개 과제** = 45개 실전 과제
- **10개 강의노트** HTML (총 487KB)
- **8개 Python 실습** Jupyter
- **5개 참고 부록** (n8n · RAG · KIS · 프롬프트 · 안전)
- **자동화 스크립트** (환경 검증 · 제출 폴더 생성)
- **GitHub 인프라** (이슈/PR 템플릿 · Actions)

전체 구조는 `REPO_STRUCTURE.txt` 참조.

---

## ⚠️ 마지막 당부

### 절대 금지

1. ❌ **API 키를 GitHub에 커밋** → 30초 내 탈취
2. ❌ **Discord 스크린샷에 키 노출** → 모자이크 필수
3. ❌ **실전 계좌로 바로 실습** → Paper Trading만 사용

### 강력 권장

1. ✅ **매 주차마다 `scripts/verify_env.py` 실행** → 환경 확인
2. ✅ **과제는 제출 폴더 자동 생성으로 시작** → 실수 방지
3. ✅ **막히면 24시간 내 질문** → 혼자 고민하지 말 것

---

<div align="center">

**🎓 준비됐나요?**

지금 `README.md`를 여세요. 8주 뒤 당신은 AI 자동매매 시스템을 직접 만든 사람이 됩니다.

[README.md 열기 →](README.md)

</div>

---

*이 문서는 `QUICK_START.md`입니다. 언제든 다시 읽을 수 있습니다.*
