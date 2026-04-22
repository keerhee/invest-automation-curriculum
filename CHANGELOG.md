# 📝 변경 이력 (CHANGELOG)

모든 주요 변경사항을 기록합니다. 형식은 [Keep a Changelog](https://keepachangelog.com/)를 따릅니다.

버전 번호는 [Semantic Versioning](https://semver.org/)을 따릅니다.

---

## [1.0.0] - 2026-04-22

### 🎉 최초 공개 릴리즈

**32개 교육 자료 전체 포함**:

#### 📘 강의노트 (10개)
- 커리큘럼 전체 개요
- W1~W8 주차별 강의노트
- KIS 모의투자 특별세션

#### 💻 Python 실습 (8개)
- W1: 3종 자산 가격 수집
- W2: 기술적 지표 계산
- W3: 뉴스 센티먼트 분석
- W4: 차트 Vision 에이전트
- W5: 스케줄링 + RAG 기초
- W6: Hybrid RAG 실전
- W7: 멀티 에이전트 오케스트레이션
- W8: Paper Trading 완성

#### 📚 참고 부록 (5개)
- A: n8n 실전 매뉴얼 (12개 노드 · 표현식 치트시트 · 에러 Top 10)
- B: Hybrid RAG 심화 가이드 (청킹 튜닝 · Reranker · Recall 측정)
- C: KIS API 통합 레퍼런스 (15+ 엔드포인트 · TR_ID 맵 · 에러 코드 20선)
- D: 프롬프트 패키지 (16개 복붙용 프롬프트 · 5가지 튜닝 패턴)
- E: 안전장치 체크리스트 (Risk Guards 4단계 · 사고 대응 프로토콜)

#### 📝 과제 워크북 (9개)
- W1~W8 + KIS 각 100점 만점
- 총 45개 과제 · 225개 루브릭 항목
- 필수 3개 + 심화 2개 구조

#### 🛠️ 리포 인프라
- README.md · SAFETY.md · FAQ.md
- CONTRIBUTING.md · CODE_OF_CONDUCT.md
- GitHub 이슈/PR 템플릿
- 환경 변수 검증 스크립트
- 과제 제출 폴더 자동 생성 스크립트

### 📐 설계 원칙

- **3차원 분석 프레임**: Price + News + Chart를 AI로 통합
- **점진적 복잡도**: W1(기초 API) → W8(실 주문) 자연스러운 진행
- **안전 최우선**: 4단계 Risk Guards + 2단계 승인 + Kill Switch
- **비용 최적화**: Haiku/Sonnet 혼용으로 $10~20 수준 유지
- **완성도**: 모든 과제 루브릭 100점 검증 완료

---

## [미공개] - Future Roadmap

### 🚧 계획 중

- **번역**: 영어·일본어·중국어 버전
- **영상 강의**: 주차별 30분 설명 비디오
- **Jupyter Book**: 전체 자료 웹사이트화
- **부록 F**: 키움증권 · 이베스트 API 추가
- **W9 (선택)**: 지속적 통합(CI/CD) · GitHub Actions 자동화
- **백테스트 엔진**: 본인 전략 검증 프레임워크

### 💡 제안 받는 중

- [GitHub Discussions](https://github.com/YOUR_ORG/invest-automation-curriculum/discussions)에서 투표 · 제안

---

## 버전 규칙

- **MAJOR** (1.x.x → 2.x.x): 커리큘럼 구조 대폭 개편
- **MINOR** (x.1.x → x.2.x): 신규 주차·부록·기능 추가
- **PATCH** (x.x.1 → x.x.2): 오타·버그·링크 수정

---

## 업데이트 알림

릴리즈 소식 받기:
- GitHub 리포 우측 상단 **Watch** → **Releases only**
- Discord `#announcements` 채널
