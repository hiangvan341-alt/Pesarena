from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML = (ROOT / 'templates' / 'room_detail.html').read_text(encoding='utf-8')
CSS = (ROOT / 'static' / 'css' / 'arena_room_v2.css').read_text(encoding='utf-8')
APP = (ROOT / 'app.py').read_text(encoding='utf-8')
ASSET = ROOT / 'static' / 'assets' / 'room_v2'

assert 'APP_VERSION = "V1.3.7"' in APP
assert "assets/room_v2/emblems/' ~ selected_rank_mode ~ '.webp'" in HTML
assert 'data-mode="{{ mode.code }}"' in HTML
assert '.arena-room-v2' in CSS
assert '!important' not in CSS

required = [
    ASSET / 'pes-arena-room-logo.webp',
    ASSET / 'vs-gold-emblem.webp',
]
for code in ['rank_random','random3_pick1','tactical_bo3','bo3','ban_pick_bo3','home_away']:
    required += [ASSET / 'modes' / f'{code}.webp', ASSET / 'emblems' / f'{code}.webp']
for path in required:
    assert path.exists() and path.stat().st_size > 0, path

print('PASS: V1.3.7 user WebP logo mapping')
