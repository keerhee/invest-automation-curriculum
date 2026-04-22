# 📝 과제 워크북

각 주차의 학습을 **자기만의 결과물**로 완성하는 과제입니다. 포트폴리오가 되는 실전 프로젝트입니다.

## 📚 전체 목록

| 파일 | 주차 | 과제 수 | 배점 |
|---|:---:|:---:|:---:|
| [W1_Homework](W1_Homework.html) | 데이터 수집 | 5 (필수 3 + 심화 2) | 100 |
| [W2_Homework](W2_Homework.html) | 기술적 지표 | 5 | 100 |
| [W3_Homework](W3_Homework.html) | 뉴스 센티먼트 | 5 | 100 |
| [W4_Homework](W4_Homework.html) | Vision + 3D | 5 | 100 |
| [W5_Homework](W5_Homework.html) | 스케줄 + Vector | 5 | 100 |
| [W6_Homework](W6_Homework.html) | Hybrid RAG | 5 | 100 |
| [W7_Homework](W7_Homework.html) | 멀티 에이전트 | 5 | 100 |
| [W8_Homework](W8_Homework.html) | Paper Trading | 5 | 100 |
| [KIS_Homework](KIS_Homework.html) | KIS 모의투자 | 5 | 100 |

**총 45개 과제 · 225개 채점 기준**

## 📋 과제 구조 (공통)

각 주차는 **5개 과제**로 구성됩니다:

### 🟢 필수 (Required) · 70점
- **Q1** — 25점 · 핵심 구현
- **Q2** — 25점 · 확장 구현
- **Q3** — 20점 · 통합 검증

### 🟡 심화 (Advanced) · 30점
- **Q4** — 15점 · 응용
- **Q5** — 15점 · 도전 과제

### 🎯 통과 기준
- **최소 통과**: 60점
- **Pass**: 70점 (필수 3개 만점)
- **A급**: 85점 이상

## 🚀 과제 시작 방법

### 1. 제출 폴더 자동 생성

```bash
# 본인 이름으로 W1 제출 폴더 생성
python scripts/generate_submission.py --week W1 --name HongGilDong

# 생성된 폴더 구조:
# submissions/W1_HongGilDong/
#   ├── README.md            (본인 회고 템플릿)
#   ├── Q1_BTC_Price.json    (워크플로 export 들어갈 자리)
#   ├── Q2_Triple_API.json
#   ├── Q3_Schedule.json
#   ├── Q4_MultiStock.json   (심화)
#   ├── Q5_Alert.json         (심화)
#   ├── screenshots/         (Q별 스크린샷)
#   └── notes/               (기타 메모)
```

### 2. 과제 워크북 열기

```bash
open W1_Homework.html
# 브라우저에서 과제 5개 + 힌트 + 채점 기준 확인
```

### 3. 진행

- 강의노트 + 실습 랩을 먼저 완료
- 과제별 "문제 상황 → 달성 목표 → 제출물 → 채점 기준 → 힌트" 순서 확인
- 힌트는 접혀있는 details 블록, 정말 막혔을 때만 펼치기

### 4. 제출

과제 워크북 하단의 "제출 가이드" 섹션 확인:
- Discord `#homework-wN` 채널에 zip 업로드
- 또는 학교/수업 공지에 따른 제출

## ⚠️ 유의사항

### 자주 감점되는 포인트
- ❌ 스크린샷에 실행 시각이 안 보임 (증명 불가)
- ❌ 워크플로 이름이 "My workflow" 그대로 (규칙 미준수)
- ❌ Google Sheets 공유 권한 "제한됨" (강사가 확인 불가)
- ❌ Executions 로그 캡처 없음 (실행 여부 검증 불가)

### API 키 보안
- ✅ **절대** 스크린샷·JSON export에 API 키 포함 금지
- ✅ JSON export 후 `"value": "..."` 부분을 빈칸으로 수정
- ✅ 스크린샷은 API 키 부분 모자이크

## 🌟 A급 과제의 특징

강사가 "이 과제는 정말 잘 했다"고 느끼는 제출물의 공통점:

1. **목표를 초과 달성** — 과제 요구보다 한 걸음 더
2. **명확한 README** — 설계 결정의 근거 설명
3. **시각적 증빙** — 스크린샷 + 다이어그램
4. **실패 공유** — 막혔던 지점과 해결 과정
5. **재사용 가능** — 다른 종목·시장에도 확장 가능한 구조

## 💡 포트폴리오 활용 팁

완성한 과제를 **취업·진학 포트폴리오**로 활용하는 방법:

1. **GitHub 공개** — 본인 계정에 별도 리포 만들기
2. **README 상세 작성** — 시스템 구조도 + 스크린샷
3. **Medium/Brunch 글** — 배운 것을 블로그로 정리
4. **포트폴리오 사이트** — notion/velog에 업로드
5. **LinkedIn 언급** — "AI 자동매매 시스템 구축 경험" 식으로

W8 과제 Q5(수료 발표 리포트)가 가장 포트폴리오로 쓰기 좋습니다.

---

[← docs/](../README.md) · [💻 실습](../labs/README.md) · [📚 부록 →](../appendix/README.md)
