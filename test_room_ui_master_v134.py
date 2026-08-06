from pathlib import Path

css = Path('static/css/room_master.css').read_text(encoding='utf-8')
assert 'body[data-page="room_detail"] .player-topbar' in css
assert '.room-layout-v137 .room-arena-frame{\n  min-height:0;' in css
assert 'min-height:405px;height:405px' in css
assert '.room-layout-v137 .room-master-mode-card{min-height:91px' in css
assert 'zoom:' not in css
assert 'transform:scale(' not in css.replace('transform:scaleX(-1)', '')
print('PASS: UI MASTER room fits desktop 100% without browser scaling')
