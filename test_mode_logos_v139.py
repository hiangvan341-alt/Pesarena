from pathlib import Path
ROOT=Path(__file__).resolve().parent

def test_mode_logo_assets_exist():
    names=['rank_random.webp','random3_pick1.webp','tactical_bo3.webp','bo3.webp','ban_pick_bo3.webp','home_away.webp']
    for sub in ['modes','emblems']:
        for name in names:
            p=ROOT/'static/assets/room_v2'/sub/name
            assert p.exists() and p.stat().st_size>100_000

def test_mode_logo_template_cache_bust():
    for rel in ['templates/room_detail.html','templates/_room_live_content.html']:
        s=(ROOT/rel).read_text(encoding='utf-8')
        assert "room_asset('modes/' ~ mode.code ~ '.webp') }}?v={{ APP_VERSION|urlencode }}" in s
        assert "room_asset('emblems/' ~ selected_rank_mode ~ '.webp') }}?v={{ APP_VERSION|urlencode }}" in s

def test_mode_logo_css_normalized():
    s=(ROOT/'static/css/room/03-mode-selector.css').read_text(encoding='utf-8')
    assert 'V1.3.39 — normalized mode-logo viewport' in s
    assert 'object-fit: contain' in s
    assert 'width: 76px' in s and 'height: 76px' in s
