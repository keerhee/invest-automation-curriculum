#!/usr/bin/env python3
"""환경변수 검증 스크립트

.env 파일의 필수 키가 모두 정상적으로 설정되었는지 확인합니다.
주차별로 필요한 키를 그룹화해서 체크할 수 있습니다.

사용법:
    python scripts/verify_env.py              # 전체 검증
    python scripts/verify_env.py --week W1    # W1에 필요한 키만
    python scripts/verify_env.py --week W6    # W6까지 누적 필요
"""

import os
import sys
import argparse
from pathlib import Path


# ═══════════════════════════════════════════════════════════
# 주차별 필수 환경변수 매핑
# ═══════════════════════════════════════════════════════════

WEEK_REQUIREMENTS = {
    'W1': {
        'FRED_API_KEY': ('FRED API · 환율·금리 지표', 'https://fred.stlouisfed.org/docs/api/api_key.html'),
    },
    'W3': {
        'ALPHA_VANTAGE_API_KEY': ('Alpha Vantage · 뉴스 센티먼트', 'https://www.alphavantage.co/support/#api-key'),
        'ANTHROPIC_API_KEY': ('Claude Haiku · 뉴스 분석', 'https://console.anthropic.com/settings/keys'),
    },
    'W4': {
        'CHART_IMG_API_KEY': ('Chart-IMG · 차트 이미지', 'https://chart-img.com/dashboard'),
    },
    'W5': {
        'OPENAI_API_KEY': ('OpenAI · Embeddings', 'https://platform.openai.com/api-keys'),
        'SUPABASE_URL': ('Supabase · Vector DB', 'https://supabase.com/dashboard'),
        'SUPABASE_SERVICE_ROLE_KEY': ('Supabase Service Role Key', '프로젝트 Settings → API'),
    },
    'W6': {
        'COHERE_API_KEY': ('Cohere · Reranker', 'https://dashboard.cohere.com/api-keys'),
    },
    'W7': {},  # W7은 위 키들 조합
    'W8': {
        'ALPACA_PAPER_API_KEY': ('Alpaca Paper · 미국 주식 모의', 'https://alpaca.markets'),
        'ALPACA_PAPER_SECRET_KEY': ('Alpaca Paper Secret', '위와 동일'),
    },
    'SP': {
        'KIS_APP_KEY': ('KIS · 한국 주식 모의', 'https://apiportal.koreainvestment.com'),
        'KIS_APP_SECRET': ('KIS App Secret', '위와 동일'),
        'KIS_ACCOUNT_NUMBER': ('KIS 모의투자 계좌번호', '위와 동일'),
    },
    'all': {
        'DISCORD_WEBHOOK_GENERAL': ('Discord 일반 알림', 'Discord 채널 설정'),
    },
}


# ═══════════════════════════════════════════════════════════
# 값 유효성 패턴 (너무 엄격하지 않게)
# ═══════════════════════════════════════════════════════════

VALIDATION_PATTERNS = {
    'ANTHROPIC_API_KEY': lambda v: v.startswith('sk-ant-'),
    'OPENAI_API_KEY': lambda v: v.startswith('sk-') and len(v) > 20,
    'ALPACA_PAPER_BASE_URL': lambda v: 'paper-api.alpaca.markets' in v,
    'KIS_BASE_URL': lambda v: 'openapivts' in v,  # 모의투자 URL인지 확인
    'SUPABASE_URL': lambda v: v.startswith('https://') and '.supabase.co' in v,
}


# ═══════════════════════════════════════════════════════════
# 출력 포매팅
# ═══════════════════════════════════════════════════════════

class Colors:
    """터미널 색상 (Windows 10 이상 / macOS / Linux)"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def ok(msg): print(f"{Colors.GREEN}✓{Colors.END} {msg}")
def fail(msg): print(f"{Colors.RED}✗{Colors.END} {msg}")
def warn(msg): print(f"{Colors.YELLOW}⚠{Colors.END} {msg}")
def info(msg): print(f"{Colors.BLUE}ℹ{Colors.END} {msg}")
def header(msg): print(f"\n{Colors.BOLD}{msg}{Colors.END}\n" + '─' * 60)


# ═══════════════════════════════════════════════════════════
# 검증 로직
# ═══════════════════════════════════════════════════════════

def load_env_file(env_path='.env'):
    """.env 파일을 읽어서 환경변수로 로드"""
    if not Path(env_path).exists():
        fail(f".env 파일을 찾을 수 없습니다: {env_path}")
        info("템플릿을 복사하세요: cp templates/env/.env.example .env")
        sys.exit(1)
    
    loaded = {}
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, _, val = line.partition('=')
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                os.environ[key] = val
                loaded[key] = val
    
    return loaded


def is_placeholder(value):
    """값이 여전히 템플릿 placeholder인지 확인"""
    placeholders = [
        'YOUR_KEY_HERE', 'YOUR_32_CHAR_KEY_HERE', 'YOUR_PAPER_KEY',
        'YOUR_PAPER_SECRET', 'YOUR_36_CHAR_KEY', 'YOUR_180_CHAR_SECRET',
        'YOUR_ACCOUNT_8DIGITS', 'YOUR_PROJECT', 'YOUR_ANON_KEY_HERE',
        'YOUR_SERVICE_ROLE_KEY_HERE', 'YOUR_WEBHOOK_URL', 'YOUR_URGENT_CHANNEL',
        'YOUR_LOG_CHANNEL', 'YOUR_SPREADSHEET_ID', 'HongGilDong',
        'your@email.com', 'YOUR_KEY', 'sk-ant-api03-YOUR_KEY_HERE',
        'sk-proj-YOUR_KEY_HERE',
    ]
    return any(p in value for p in placeholders)


def validate_key(key, value):
    """개별 키의 유효성 검증"""
    if not value:
        return False, "값이 비어있음"
    if is_placeholder(value):
        return False, "아직 템플릿 값 (변경 필요)"
    
    if key in VALIDATION_PATTERNS:
        if not VALIDATION_PATTERNS[key](value):
            return False, "값 형식이 예상과 다름"
    
    # 기본 검증: 충분한 길이
    if len(value) < 10 and not key.endswith('_URL') and not key.endswith('CODE'):
        return False, f"값이 너무 짧음 ({len(value)}자)"
    
    return True, "OK"


def mask_value(value):
    """키 값을 일부만 보여주기 (보안)"""
    if len(value) < 12:
        return '*' * len(value)
    return value[:6] + '***' + value[-4:]


def check_requirements_for_week(week, loaded_vars):
    """특정 주차까지 필요한 키 검증"""
    target_weeks = []
    week_order = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'SP']
    
    if week == 'all':
        target_weeks = week_order + ['all']
    elif week in week_order:
        idx = week_order.index(week)
        target_weeks = week_order[:idx+1] + ['all']
    else:
        fail(f"알 수 없는 주차: {week}")
        return
    
    total_required = 0
    total_ok = 0
    issues = []
    
    for w in target_weeks:
        if w not in WEEK_REQUIREMENTS:
            continue
        
        reqs = WEEK_REQUIREMENTS[w]
        if not reqs:
            continue
        
        header(f"📋 {w} 필수 환경변수")
        
        for key, (desc, url) in reqs.items():
            total_required += 1
            value = os.environ.get(key, '')
            valid, reason = validate_key(key, value)
            
            if valid:
                ok(f"{key:<30} {desc} · {mask_value(value)}")
                total_ok += 1
            else:
                fail(f"{key:<30} {desc}")
                issues.append((key, reason, url))
    
    # 결과 요약
    header("📊 검증 결과")
    if total_ok == total_required:
        ok(f"모든 필수 키 정상 설정 완료 ({total_ok}/{total_required})")
        info(f"{week} 주차 실습을 시작할 수 있습니다!")
    else:
        warn(f"설정 필요: {total_required - total_ok}개 / 전체 {total_required}개")
        print()
        for key, reason, url in issues:
            fail(f"{key}")
            print(f"   이유: {reason}")
            print(f"   발급: {url}")
            print()
        
        info("해결 후 다시 실행: python scripts/verify_env.py --week " + week)


def main():
    parser = argparse.ArgumentParser(
        description='환경변수 검증 스크립트',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--week',
        default='all',
        choices=['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'SP', 'all'],
        help='검증할 주차 (기본: all)'
    )
    parser.add_argument(
        '--env',
        default='.env',
        help='환경 파일 경로 (기본: .env)'
    )
    args = parser.parse_args()
    
    print(f"{Colors.BOLD}🔍 환경변수 검증 시작{Colors.END}")
    info(f"대상 주차: {args.week}")
    info(f"환경 파일: {args.env}")
    
    loaded = load_env_file(args.env)
    ok(f".env 파일 로드 완료 ({len(loaded)}개 변수)")
    
    check_requirements_for_week(args.week, loaded)
    
    print(f"\n{Colors.BOLD}🎯 팁{Colors.END}")
    info("특정 주차만 검증: python scripts/verify_env.py --week W3")
    info("다른 환경 파일: python scripts/verify_env.py --env .env.production")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n검증이 중단되었습니다.")
        sys.exit(0)
    except Exception as e:
        fail(f"예기치 않은 오류: {e}")
        sys.exit(1)
