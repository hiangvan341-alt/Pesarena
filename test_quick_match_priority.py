from pathlib import Path

SOURCE = Path(__file__).with_name("app.py").read_text(encoding="utf-8")


def test_quick_match_priority_groups_present():
    assert "same_rank = get_rank_level(opponent_points) == my_rank_level" in SOURCE
    assert "elif gap <= 300:" in SOURCE
    assert "elif gap <= 500:" in SOURCE
    assert "elif gap <= 1000:" in SOURCE
    assert "elif gap <= 2000:" in SOURCE
    assert "priority_group, gap, seen_sort" in SOURCE


def test_quick_match_excludes_over_2000_for_different_rank():
    marker = "elif gap <= 2000:"
    start = SOURCE.index(marker)
    block = SOURCE[start:start + 180]
    assert "else:" in block
    assert "continue" in block


def test_quick_match_sort_order():
    assert "candidates.sort(key=lambda item: (item[0], item[1], item[2], item[3]))" in SOURCE
