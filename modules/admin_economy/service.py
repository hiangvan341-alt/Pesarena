"""Nghiệp vụ hiển thị trang quản trị kinh tế riêng."""

import uuid

from . import repository


def configure(context):
    globals().update(context)
    repository.configure(context)


def _safe_load(label, loader, default):
    try:
        value = loader()
        return default if value is None else value
    except Exception as exc:
        app.logger.exception("Admin economy load failed [%s]: %s", label, exc)
        return default


def build_page_context(actor):
    """Mọi tài khoản Admin hợp lệ đều có toàn quyền kinh tế theo cấu hình app."""
    players = _safe_load("players", repository.list_players_for_economy, [])
    transactions = _safe_load(
        "zcoin_transactions",
        lambda: repository.list_recent_transactions(limit=100),
        [],
    )
    gift_codes = _safe_load(
        "gift_codes",
        lambda: repository.list_codes(limit=150),
        [],
    )
    stats = build_zcoin_stats(players, transactions)
    return {
        "players": players,
        "zcoin_transactions": transactions,
        "zcoin_stats": stats,
        "gift_codes": gift_codes,
        "zcoin_adjustment_token": uuid.uuid4().hex,
        "can_manage_zcoin": True,
        "can_manage_gift_codes": True,
    }
