from pathlib import Path

def test_bottom_logo_final_override_is_in_later_css_module():
    css = Path('static/css/room/04-actions-history.css').read_text(encoding='utf-8')
    assert 'V1.3.44 — BOTTOM MODE LOGOS ONLY.' in css
    assert 'transform: scale(2.65)' in css
    assert 'grid-template-columns: 82px minmax(0,1fr)' in css

def test_active_mode_logo_is_magnified_without_layout_growth():
    css = Path('static/css/room/03-mode-selector.css').read_text(encoding='utf-8')
    assert 'V1.3.44 — ACTIVE MODE LOGO ONLY.' in css
    assert 'transform: scale(2.45)' in css
    assert 'overflow: hidden' in css
