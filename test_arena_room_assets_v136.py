from pathlib import Path
ROOT=Path(__file__).resolve().parent
assets=ROOT/'static/assets/room_v2'
required=['pes-arena-room-logo.webp','stadium-blue.webp','stadium-red.webp','light-effect-blue.webp','light-effect-red.webp','vs-gold-emblem.webp','parsec-logo.webp','share-link.webp']
for name in required: assert (assets/name).exists(), name
for code in ['rank_random','random3_pick1','tactical_bo3','bo3','ban_pick_bo3','home_away']: assert (assets/'modes'/f'{code}.webp').exists(), code
css=(ROOT/'static/css/arena_room_v2.css').read_text(encoding='utf-8')
assert '.arena-room-v2' in css
assert '!important' not in css
assert 'stadium-blue.webp' in css and 'stadium-red.webp' in css
html=(ROOT/'templates/room_detail.html').read_text(encoding='utf-8')
assert "assets/room_v2/modes/" in html and 'vs-gold-emblem.webp' in html
print('PASS: Arena Room V1.3.6 assets and CSS')
