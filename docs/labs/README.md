# 💻 Python 실습 (Jupyter Notebook)

각 주차의 핵심 개념을 **실제 코드로** 확인하는 실습 파일입니다. 강의노트를 읽은 후 바로 실행해보세요.

## 📚 전체 목록

| 파일 | 주제 | 핵심 라이브러리 |
|---|---|---|
| [W1_Lab.ipynb](W1_Lab.ipynb) | 가격 데이터 수집 | `requests`, `yfinance`, `pandas` |
| [W2_Lab.ipynb](W2_Lab.ipynb) | 기술적 지표 계산 | `pandas`, `numpy`, `matplotlib` |
| [W3_Lab.ipynb](W3_Lab.ipynb) | 뉴스 센티먼트 분석 | `anthropic`, `requests` |
| [W4_Lab.ipynb](W4_Lab.ipynb) | Vision + 3D Agent | `anthropic`, `PIL`, `base64` |
| [W5_Lab.ipynb](W5_Lab.ipynb) | 스케줄링 + RAG 기초 | `openai`, `supabase` |
| [W6_Lab.ipynb](W6_Lab.ipynb) | Hybrid RAG | `cohere`, `openai`, `supabase` |
| [W7_Lab.ipynb](W7_Lab.ipynb) | 멀티 에이전트 | `anthropic` (Tool Use) |
| [W8_Lab.ipynb](W8_Lab.ipynb) | Paper Trading | `alpaca-py` |

## 🚀 실행 방법

### 옵션 1: Google Colab (가장 쉬움)

```
1. https://colab.research.google.com 접속
2. "파일" → "업로드" → .ipynb 파일 선택
3. "Runtime" → "Run all"
```

**장점**: 설치 불필요 · 무료 · 브라우저만 있으면 됨  
**단점**: API 키 입력을 매 세션마다

### 옵션 2: 로컬 Jupyter

```bash
# 1. 가상환경 생성 (권장)
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate            # Windows

# 2. 필요 라이브러리 설치
pip install jupyter anthropic openai pandas yfinance requests \
            matplotlib supabase cohere alpaca-py python-dotenv

# 3. Jupyter 실행
jupyter notebook

# 4. 브라우저가 열리면 W1_Lab.ipynb 클릭
```

### 옵션 3: VS Code

1. VS Code 설치 + Python 확장 설치
2. Jupyter 확장도 설치
3. .ipynb 파일을 VS Code에서 직접 열기
4. 우측 상단 "Python 환경 선택" → venv 선택
5. 각 셀 옆 ▷ 버튼으로 실행

## 🔐 API 키 설정

실습 파일 상단 셀에 다음 패턴이 있습니다:

```python
import os
from dotenv import load_dotenv

load_dotenv()  # 프로젝트 루트의 .env 파일 로드

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
```

**.env 파일이 프로젝트 루트에 있어야 합니다**. 템플릿은 [`templates/env/.env.example`](../../templates/env/.env.example) 참조.

## ⚠️ 실행 전 체크

- [ ] `.env` 파일에 필요한 API 키가 설정되었는가?
- [ ] 필요한 라이브러리가 설치되었는가?
- [ ] 인터넷 연결이 되어 있는가? (대부분 API 호출 필요)

검증:
```bash
python scripts/verify_env.py --week W1
```

## 💡 실습 팁

1. **한 셀씩 실행** — 전체 실행보다는 셀별로 결과 확인하며 진행
2. **수정해보기** — 코드를 그대로 따라만 하지 말고, 파라미터를 바꿔보거나 종목을 다르게 넣어보기
3. **에러는 배움의 기회** — 에러 메시지를 구글 검색하거나 Claude에게 물어보기
4. **주석 작성** — 이해한 내용을 한국어 주석으로 남기면 복습 시 큰 도움

---

[← docs/](../README.md) · [📖 강의노트](../lectures/README.md) · [📝 과제 →](../homework/README.md)
