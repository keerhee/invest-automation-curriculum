#!/usr/bin/env python3
"""과제 제출 폴더 자동 생성 스크립트

주차별 과제 제출용 표준 폴더 구조를 자동으로 생성합니다.

사용법:
    python scripts/generate_submission.py --week W1 --name HongGilDong
    python scripts/generate_submission.py --week KIS --name JohnDoe
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime


# ═══════════════════════════════════════════════════════════
# 주차별 과제 메타데이터
# ═══════════════════════════════════════════════════════════

WEEK_ASSIGNMENTS = {
    'W1': {
        'title': '데이터 수집 자동화',
        'tasks': [
            ('Q1', 'BTC_Price', 'required', 25),
            ('Q2', 'Triple_API', 'required', 25),
            ('Q3', 'Schedule', 'required', 20),
            ('Q4', 'MultiStock', 'advanced', 15),
            ('Q5', 'Alert', 'advanced', 15),
        ],
    },
    'W2': {
        'title': '기술적 지표 계산',
        'tasks': [
            ('Q1', 'RSI_14', 'required', 25),
            ('Q2', 'MA_Cross', 'required', 25),
            ('Q3', 'Bollinger', 'required', 20),
            ('Q4', 'MACD_EMA', 'advanced', 15),
            ('Q5', 'Composite', 'advanced', 15),
        ],
    },
    'W3': {
        'title': '뉴스 센티먼트 분석',
        'tasks': [
            ('Q1', 'AV_News', 'required', 25),
            ('Q2', 'Claude_News', 'required', 25),
            ('Q3', 'Aggregate', 'required', 20),
            ('Q4', 'TwoDim', 'advanced', 15),
            ('Q5', 'Backtest', 'advanced', 15),
        ],
    },
    'W4': {
        'title': '차트 Vision + 3D Verdict',
        'tasks': [
            ('Q1', 'ChartIMG', 'required', 25),
            ('Q2', 'Vision', 'required', 25),
            ('Q3', 'ThreeDim', 'required', 20),
            ('Q4', 'MultiInterval', 'advanced', 15),
            ('Q5', 'PDFReport', 'advanced', 15),
        ],
    },
    'W5': {
        'title': '스케줄링 + Vector DB 기초',
        'tasks': [
            ('Q1', 'MultiSchedule', 'required', 25),
            ('Q2', 'Supabase', 'required', 25),
            ('Q3', 'FirstRAG', 'required', 20),
            ('Q4', 'MetaFilter', 'advanced', 15),
            ('Q5', 'Briefing', 'advanced', 15),
        ],
    },
    'W6': {
        'title': 'Hybrid RAG 실전',
        'tasks': [
            ('Q1', 'PDFIngest', 'required', 25),
            ('Q2', 'HybridRAG', 'required', 25),
            ('Q3', 'Citation', 'required', 20),
            ('Q4', 'Recall', 'advanced', 15),
            ('Q5', 'PersonalRAG', 'advanced', 15),
        ],
    },
    'W7': {
        'title': '멀티 에이전트 오케스트레이션',
        'tasks': [
            ('Q1', 'SubAgents', 'required', 25),
            ('Q2', 'Orchestrator', 'required', 25),
            ('Q3', 'MessageBus', 'required', 20),
            ('Q4', 'KoreanAgent', 'advanced', 15),
            ('Q5', 'CostOpt', 'advanced', 15),
        ],
    },
    'W8': {
        'title': 'Paper Trading + 수료',
        'tasks': [
            ('Q1', 'Alpaca', 'required', 25),
            ('Q2', 'Guards', 'required', 25),
            ('Q3', 'Bracket', 'required', 20),
            ('Q4', 'WeeklyReport', 'advanced', 15),
            ('Q5', 'FinalReport', 'advanced', 15),
        ],
    },
    'KIS': {
        'title': 'KIS 모의투자 특별세션',
        'tasks': [
            ('Q1', 'Token', 'required', 25),
            ('Q2', 'Quote', 'required', 25),
            ('Q3', 'BuyOrder', 'required', 20),
            ('Q4', 'TickSize', 'advanced', 15),
            ('Q5', 'AIToKIS', 'advanced', 15),
        ],
    },
}


README_TEMPLATE = """# {week} 과제 제출 — {name}

**제출자**: {name}  
**주차**: {week} · {title}  
**제출일**: {date}  
**완료 과제**: __개 / 5개

---

## 📋 제출물 체크리스트

{checklist}

---

## 💭 회고

### 이번 주차에서 가장 어려웠던 점

<!-- 막혔던 지점, 어떻게 해결했는지 3~5줄로 -->

### 가장 재미있었던 부분

<!-- 배움의 기쁨, 새로 알게 된 것 -->

### 개선하고 싶은 점

<!-- 더 잘할 수 있었던 부분, 다음 주에 시도할 것 -->

---

## 📎 첨부 파일 안내

- 워크플로 JSON: 각 Q별 export
- 스크린샷: `screenshots/` 폴더
- 추가 설명: 필요 시 `notes/` 폴더

---

## 🎯 자체 평가

총 점수: __ / 100점 (본인 평가)

| 과제 | 본인 평가 | 근거 |
|:---:|:---:|---|
{self_rubric}

---

*생성일: {date}*  
*스크립트: `python scripts/generate_submission.py`*
"""


# ═══════════════════════════════════════════════════════════
# 생성 로직
# ═══════════════════════════════════════════════════════════

def create_submission_folder(week, name, output_dir='submissions'):
    """제출용 폴더 구조 생성"""
    
    if week not in WEEK_ASSIGNMENTS:
        print(f"❌ 알 수 없는 주차: {week}")
        print(f"   사용 가능: {', '.join(WEEK_ASSIGNMENTS.keys())}")
        sys.exit(1)
    
    week_info = WEEK_ASSIGNMENTS[week]
    folder_name = f"{week}_{name}"
    base_path = Path(output_dir) / folder_name
    
    # 이미 존재하는지 확인
    if base_path.exists():
        response = input(f"⚠️  {base_path}가 이미 존재합니다. 덮어쓸까요? [y/N]: ")
        if response.lower() != 'y':
            print("중단되었습니다.")
            sys.exit(0)
    
    # 폴더 구조 생성
    base_path.mkdir(parents=True, exist_ok=True)
    (base_path / 'screenshots').mkdir(exist_ok=True)
    (base_path / 'notes').mkdir(exist_ok=True)
    
    # 각 과제별 placeholder JSON
    for code, slug, task_type, points in week_info['tasks']:
        filename = f"{code}_{slug}.json"
        placeholder = {
            "_comment": f"{code} 워크플로 export를 여기 붙여넣으세요",
            "_task_info": {
                "code": code,
                "name": slug,
                "type": task_type,
                "points": points,
                "status": "not_started"
            }
        }
        
        import json
        with open(base_path / filename, 'w', encoding='utf-8') as f:
            json.dump(placeholder, f, ensure_ascii=False, indent=2)
    
    # README 생성
    checklist_lines = []
    self_rubric_lines = []
    
    for code, slug, task_type, points in week_info['tasks']:
        badge = "🟢 필수" if task_type == 'required' else "🟡 심화"
        checklist_lines.append(
            f"- [ ] **{code}** ({badge} · {points}점): `{code}_{slug}.json` + 스크린샷"
        )
        self_rubric_lines.append(
            f"| {code} | __ / {points} | |"
        )
    
    readme_content = README_TEMPLATE.format(
        week=week,
        name=name,
        title=week_info['title'],
        date=datetime.now().strftime('%Y-%m-%d'),
        checklist='\n'.join(checklist_lines),
        self_rubric='\n'.join(self_rubric_lines),
    )
    
    with open(base_path / 'README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    # .gitkeep for empty folders
    (base_path / 'screenshots' / '.gitkeep').touch()
    (base_path / 'notes' / '.gitkeep').touch()
    
    # 결과 출력
    print(f"\n✅ 제출 폴더 생성 완료!\n")
    print(f"📂 {base_path}/")
    print(f"├── README.md")
    for code, slug, task_type, points in week_info['tasks']:
        marker = "🟢" if task_type == 'required' else "🟡"
        print(f"├── {marker} {code}_{slug}.json  ({points}점)")
    print(f"├── screenshots/")
    print(f"└── notes/")
    
    print(f"\n💡 다음 단계:")
    print(f"   1. README.md를 열어 체크리스트 확인")
    print(f"   2. 과제 워크북 확인: docs/homework/{week}_Homework.html")
    print(f"   3. 완료한 과제의 JSON export를 해당 파일에 덮어쓰기")
    print(f"   4. 스크린샷을 screenshots/ 폴더에 저장")
    print(f"   5. README.md의 회고 섹션 작성")
    print(f"   6. Discord #homework-{week.lower()} 채널에 zip 업로드\n")


def main():
    parser = argparse.ArgumentParser(
        description='과제 제출 폴더 자동 생성',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  python scripts/generate_submission.py --week W1 --name HongGilDong
  python scripts/generate_submission.py --week KIS --name JohnDoe
  python scripts/generate_submission.py --week W8 --name Alice --dir my_submissions
"""
    )
    parser.add_argument(
        '--week',
        required=True,
        choices=list(WEEK_ASSIGNMENTS.keys()),
        help='주차 (W1~W8, KIS)'
    )
    parser.add_argument(
        '--name',
        required=True,
        help='본인 이름 (영문 권장)'
    )
    parser.add_argument(
        '--dir',
        default='submissions',
        help='제출 폴더 루트 (기본: submissions)'
    )
    
    args = parser.parse_args()
    create_submission_folder(args.week, args.name, args.dir)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n중단되었습니다.")
        sys.exit(0)
