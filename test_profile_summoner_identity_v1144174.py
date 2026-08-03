from pathlib import Path

ROOT = Path(__file__).resolve().parent

def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")

def test_profile_summoner_identity_release():
    assert 'APP_VERSION = "V1.14.41.74"' in read("app.py")

def test_profile_summoner_identity_hero_is_scoped_and_complete():
    template = read("templates/profile.html")
    css = read("static/css/profile_showcase.css")
    for token in (
        "profile-v2-summoner-hero",
        "profile-v2-summoner-layout",
        "profile-v2-summoner-identity",
        "profile-v2-avatar-level",
        "profile-v2-crest-line",
        "profile-v2-mini-id-row",
        "profile-v2-honor-row",
        "profile-v2-honor-chip",
        "PES ARENA PROFILE",
    ):
        assert token in template or token in css
    assert "object-fit:contain" in css
    assert "Scoped to .profile-v2-page" in css

def test_profile_summoner_identity_keeps_existing_profile_features():
    template = read("templates/profile.html")
    for token in (
        'data-profile-tab="overview"',
        'data-profile-tab="achievements"',
        'data-profile-tab="matches"',
        'data-profile-tab="settings"',
        "Quản lý trang bị",
        "Cửa hàng",
        "data-profile-share",
        "update_parsec_id",
        "update_display_name",
        "update_profile_avatar",
        "change_password",
    ):
        assert token in template
