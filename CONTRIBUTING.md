# 🤝 기여 가이드 (CONTRIBUTING.md)

이 커리큘럼은 여러분의 기여로 더 나아집니다! 수강생, 조교, 강사, 전문가 누구나 환영합니다.

---

## 🎯 기여할 수 있는 것

### 📝 콘텐츠 개선
- 오타·문법 수정
- 설명이 부족한 부분 보강
- 더 나은 예시·비유 추가
- 번역 (영어·일본어·중국어 등)

### 🐛 버그 리포트
- 코드 오류 (Python 랩 · 워크플로 JSON)
- 링크 깨짐
- API 변경으로 동작하지 않는 예시
- 잘못된 채점 기준

### 💡 신규 자료
- 추가 실습 예제
- 새로운 자산군 가이드 (선물·옵션 등)
- 다른 증권사 API 연동 예시
- 커뮤니티 FAQ 답변

### 🎓 경험 공유
- 수료생 후기 (`EXPERIENCES/` 폴더)
- 본인 프로젝트 쇼케이스
- 막혔던 문제와 해결 방법

---

## 🚀 기여 절차

### 1. 이슈 먼저 열기

코드 변경 전에 **이슈를 열어 논의**하는 것이 효율적입니다:

```
https://github.com/YOUR_ORG/invest-automation-curriculum/issues/new/choose
```

이슈 템플릿을 사용해 명확히 작성하세요.

### 2. 포크 후 작업 브랜치 생성

```bash
# 본인 계정으로 포크 후
git clone https://github.com/YOUR_USERNAME/invest-automation-curriculum.git
cd invest-automation-curriculum

# 작업 브랜치 생성 (설명적 이름)
git checkout -b fix/w3-alpha-vantage-typo
# 또는
git checkout -b feat/w9-kiwoom-api-appendix
```

### 3. 변경사항 작업

#### HTML 문서 수정 시
- 가능한 **최소 변경**으로 유지 (스타일 전체 수정은 큰 PR)
- 링크·이미지 경로 깨지지 않는지 확인
- 한국어/영어 일관성 유지

#### 코드 수정 시 (Python 랩 등)
- 기존 스타일 유지
- 주석을 한국어로 (수강생 친화적)
- 실제로 돌려본 후 커밋

#### 과제 워크북 수정 시
- 루브릭 총합 **100점** 유지
- 필수 3 + 심화 2 구조 유지
- 너무 어려운 과제는 심화로, 쉬우면 필수로

### 4. 커밋 메시지 규칙

[Conventional Commits](https://www.conventionalcommits.org/)를 따릅니다:

```
type(scope): 한글 짧은 설명

상세 설명 (선택)
```

**type 종류**:
- `fix`: 버그 수정
- `feat`: 신규 기능/자료 추가
- `docs`: 문서 수정
- `style`: 포맷팅·오타 (기능 영향 없음)
- `refactor`: 리팩터링
- `chore`: 빌드·설정 변경

**예시**:
```
fix(w3): Alpha Vantage 엔드포인트 오류 수정
feat(appendix): 키움증권 API 부록 F 추가
docs(readme): 설치 가이드에 macOS 섹션 추가
style(w5): 코드블록 하이라이팅 색상 통일
```

### 5. Pull Request 열기

PR 템플릿을 사용해 다음을 작성:

- **어떤 문제를 해결하는가**
- **어떻게 해결했는가**
- **테스트 방법** (리뷰어가 검증할 수 있도록)
- **관련 이슈 번호** (Closes #123 형식)

### 6. 리뷰 대응

- 리뷰어의 제안은 **배우는 기회**로 생각하세요
- 동의하면 반영, 동의하지 않으면 근거와 함께 토론
- 24~72시간 내에 응답 (오래 방치하면 닫힐 수 있음)

---

## 📋 기여 체크리스트

PR 열기 전 확인:

- [ ] 이슈에서 논의된 범위 내인가?
- [ ] 링크·이미지·코드 경로가 깨지지 않는가?
- [ ] 커밋 메시지가 Conventional Commits 형식인가?
- [ ] SAFETY.md의 안전 수칙에 위배되지 않는가?
- [ ] 입문자 수준에서 이해 가능한가? (너무 전문 용어 난무 금지)
- [ ] API 키·개인정보가 노출되지 않았는가?

---

## 🎨 스타일 가이드

### HTML 문서

- 최대 너비: **720px** (모바일 친화적)
- 기본 폰트: Noto Sans KR + JetBrains Mono
- 섹션 구분: `<hr>` 또는 스타일된 divider
- 코드 블록: dark theme (#0d1117) + 한국어 주석

### Python 코드

```python
# ✅ 좋은 예
def calculate_rsi(prices: list[float], period: int = 14) -> float:
    """RSI(Relative Strength Index)를 계산한다.
    
    Args:
        prices: 종가 리스트 (오래된 것부터)
        period: 계산 기간 (기본 14)
    
    Returns:
        0~100 사이의 RSI 값
    """
    # 구현...

# ❌ 나쁜 예
def calc(p, n=14):  # 타입 힌트 없음, docstring 없음
    # 구현...
```

### 한국어 작성

- 존댓말/반말 섞지 않기 (강의노트는 존댓말, 코드 주석은 평서문)
- 영어 용어는 괄호로 병기: "강화학습(Reinforcement Learning)"
- 과도한 이모지 피하기 (1개 단락에 최대 1개)

---

## 🏆 기여자 인정

- 모든 기여자는 `CONTRIBUTORS.md`에 등재
- 의미 있는 기여 3회 이상 시 **Core Contributor** 배지
- 연 1회 우수 기여자 선정 + 공개 감사

---

## 💬 도움이 필요하면

- **Discord**: `#contributors` 채널
- **이메일**: `curriculum@example.com` (예시)
- **첫 기여가 처음이라면**: `good first issue` 라벨이 붙은 이슈부터!

---

<div align="center">

**여러분의 기여가 다음 수강생들에게 도움이 됩니다. 감사합니다! 🙏**

</div>
