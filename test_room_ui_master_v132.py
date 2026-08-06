from pathlib import Path
ROOT=Path(__file__).resolve().parent
html=(ROOT/'templates/room_detail.html').read_text(encoding='utf-8')
css=(ROOT/'static/css/room_master.css').read_text(encoding='utf-8')
app=(ROOT/'app.py').read_text(encoding='utf-8')
assert 'room-master-brand' in html
assert 'room-master-active-mode' in html
assert 'room-master-mode-grid' in html
assert html.count("url_for('room_select_ranked_mode'") == 2  # selector cũ ẩn + selector UI MASTER
assert 'Tổng điểm:' in css and 'OVR' not in css
assert all(block.strip().startswith('.room-layout-v137') or block.strip().startswith('/*') or block.strip().startswith('@media') for block in css.split('}') if block.strip() and not block.strip().startswith('@media') and not block.strip().startswith('/*'))
assert 'APP_VERSION = "V1.3.2"' in app
assert (ROOT/'docs/PES_ARENA_UPDATE_LATEST.sql').exists()
assert (ROOT/'docs/sql_archive').is_dir()
print('PASS: UI MASTER V1.3.2')
