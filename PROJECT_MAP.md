# PES ARENA — PROJECT MAP

> Mục đích: tra nhanh **lỗi nào → đọc file nào**, tránh phải quét toàn bộ dự án mỗi lần sửa.
> Cập nhật: V1.3.61 — 08/08/2026 (Asia/Bangkok)

## 1. Quy tắc FIX NHANH

Khi xử lý lỗi, đọc theo thứ tự:

1. `PROJECT_MAP.md` → xác định module sở hữu.
2. File Frontend liên quan → HTML/JS/CSS đúng phạm vi.
3. File Backend route/service/repository tương ứng.
4. Bảng Supabase/chức năng DB nếu luồng có ghi/đọc dữ liệu.
5. `logs/pes_arena.log` hoặc Vercel log → lọc theo `request_id`.
6. Chạy test đúng module trước; chỉ chạy full test khi thay đổi dependency chung.

Không sửa module khác nếu chưa chứng minh dependency liên quan.

---

## 2. Bootstrap / App core

| Khu vực | File chính | Trách nhiệm |
|---|---|---|
| Flask bootstrap | `app.py` | tạo Flask app, env, request hooks, các route legacy chưa tách |
| Date/time | `modules/datetime_utils.py` | UTC/VN datetime helpers |
| Cache | `modules/cache_utils.py` | request cache + TTL cache |
| Logging | `modules/observability/app_logging.py` | request ID, request timing, exception, JSONL log |
| System settings | `modules/core/system_settings_runtime.py` | feature toggle, Quick Match config, repeat-opponent config, maintenance |
| Dispute evidence | `modules/core/dispute_evidence.py` | validate/resize/upload/sign URL ảnh tranh chấp |
| Static assets | `modules/static_asset_service.py` | URL asset Supabase/static |
| Session runtime | `modules/session_runtime_service.py` | idle timeout / session guard |
| System feature service | `modules/system_feature_service.py` | post-login/dashboard behavior |

### Core compatibility modules

`app.py` vẫn bind public function từ `modules/core/*` vào `globals()` để route cũ không bị vỡ import.

| Module | Trách nhiệm |
|---|---|
| `modules/core/achievements.py` | thành tích người chơi |
| `modules/core/rank_team_service.py` | rank range, team pool, Smart Random |
| `modules/core/room_runtime.py` | room timeout/read model/enrichment |
| `modules/core/user_repository.py` | user/device/admin reads |
| `modules/core/match_repository.py` | match/dispute/invite reads |
| `modules/core/social_runtime.py` | announcement/chat/streak data |
| `modules/core/matchmaking_runtime.py` | active room/match/busy snapshot |

---

## 3. Phòng đấu

### Frontend

| Thành phần | File |
|---|---|
| Orchestrator | `templates/room_detail.html` |
| Topbar | `templates/room/_topbar.html` |
| Chủ phòng | `templates/room/_host_card.html` |
| Trung tâm trận đấu | `templates/room/_center_stage.html` |
| Đối thủ | `templates/room/_guest_card.html` |
| Parsec/chat rail | `templates/room/_side_rail.html` |
| Mode + lịch sử | `templates/room/_bottom_modes_history.html` |
| Extra controls | `templates/room/_extra_controls.html` |
| Runtime/polling | `templates/room/scripts/_room_runtime.html` |
| Chat | `templates/room/scripts/_room_chat.html` |
| Dialog | `templates/room/scripts/_room_dialogs.html` |
| CSS room | `static/css/room/` |

### Backend

| Luồng | File |
|---|---|
| Vào/thoát/ready/kick phòng | `modules/room_access_routes.py` |
| Chọn/quay CLB | `modules/room_team_routes.py` |
| Kết quả/xác nhận/tranh chấp | `modules/room_result_routes.py` + `modules/match_result_service.py` |
| Đá tiếp/rematch | `modules/room_rematch_routes.py` |
| State/timeout/read model | `modules/core/room_runtime.py` + route state còn trong `app.py` |
| Lịch sử trận | `modules/match_history_routes.py` |
| Ảnh bằng chứng | `modules/core/dispute_evidence.py` |

---

## 4. Rank / RP / chế độ thi đấu

| Chức năng | File chính |
|---|---|
| Công thức RP | `modules/rp_formula.py` |
| Engine tính delta | `modules/rp_engine.py` |
| Daily Rank limit | `modules/daily_rank_limit_service.py` |
| Repeat opponent factor | `modules/repeat_opponent_rp_service.py` |
| Inactivity RP | `modules/inactivity_rp_service.py` |
| Weekly reward | `modules/weekly_rp_rewards_service.py` |
| Catalog mode | `modules/rank_modes/catalog.py` |
| Unlock / điều kiện mode | `modules/rank_modes/service.py` |
| Bật/tắt mode | `modules/rank_mode_toggle/service.py` |
| Series orchestrator | `modules/rank_series/service.py` |
| Series DB | `modules/rank_series/repository.py` |
| Series routes | `modules/rank_series/routes.py` |
| Lượt đi/về | `modules/rank_series/modes/home_away.py` |
| BO3 | `modules/rank_series/modes/bo3.py` |
| Tactical BO3 | `modules/rank_series/modes/tactical_bo3.py` |
| Ban/Pick BO3 | `modules/rank_series/modes/ban_pick_bo3.py` |

---

## 5. Invite / Presence / Quick Match

> **V1.3.61: chưa di chuyển route legacy khỏi `app.py`** vì nhiều regression test đang kiểm tra source trực tiếp.

| Luồng | File |
|---|---|
| Gửi/nhận/cancel invite | route legacy trong `app.py` + `modules/invites/service.py` |
| Online/offline | `modules/presence/service.py` + heartbeat route trong `app.py` |
| Quick Match priority | `modules/quick_match/service.py` + route legacy trong `app.py` |
| Busy/active match | `modules/core/matchmaking_runtime.py` |
| Quick Match config | `modules/core/system_settings_runtime.py` |

Khi sửa Invite/Quick Match: **không chuyển route sang file khác trong cùng bản fix**, trừ khi cập nhật toàn bộ source-based regression test cùng lúc.

---

## 6. Người dùng / Profile / Auth

| Chức năng | File |
|---|---|
| Login/register/password/logout | route legacy trong `app.py` |
| User repository | `modules/core/user_repository.py` |
| Profile routes | `modules/profile/routes.py` |
| Profile service | `modules/profile/service.py` |
| Profile repository | `modules/profile/repository.py` |
| Equipment/badge | `modules/profile/equipment_service.py` |

---

## 7. Admin

| Tab/luồng | File |
|---|---|
| Dashboard | `modules/admin_dashboard_routes.py` |
| System | `modules/admin_system_routes.py` |
| Account | `modules/admin_account_routes.py` |
| Match | `modules/admin_match_routes.py` |
| Player | `modules/admin_player_routes.py` |
| Data | `modules/admin_data_routes.py` |
| Economy | `modules/admin_economy/` |
| Shop | `modules/admin_shop/` |
| Ranking rebuild | `modules/admin_ranking_rebuild.py` + `modules/ranking_rebuild_service.py` |
| System settings runtime | `modules/core/system_settings_runtime.py` |

---

## 8. Economy / Shop

| Chức năng | File |
|---|---|
| Zcoin | `modules/zcoin/` |
| Daily Check-in | `modules/daily_checkin/` |
| Gift Codes | `modules/gift_codes/` |
| Shop | `modules/shop/` |
| Inventory | `modules/inventory/` |
| Lucky Box | `modules/luckybox/` |

---

## 9. Parsec

| Chức năng | File |
|---|---|
| Routes | `modules/parsec_room/routes.py` |
| Service | `modules/parsec_room/service.py` |
| UI | `templates/room/_side_rail.html` và partial liên quan |

---

## 10. CSS / Assets

| Khu vực | File |
|---|---|
| Compatibility CSS entry | `static/style.css` |
| Legacy CSS frozen | `static/css/legacy/` |
| Room CSS | `static/css/room/` |
| Admin CSS | `static/css/admin/` nếu có |
| Asset helper | `modules/static_asset_service.py` |
| Supabase manifest | `SUPABASE_ASSET_MANIFEST.csv` |

**Quy tắc:** lỗi logic không sửa CSS. Lỗi hiển thị mới kiểm tra cascade/scoped selector.

---

### Chính sách ảnh từ V1.3.62

- Ảnh UI dùng chung: Supabase `pes-assets/v1/` — không giữ bản local trùng lặp.
- Ảnh Shop: Supabase `pes-assets/v1.14.41/shop/`.
- Lucky Box: Supabase `pes-assets/v1.14.41/luckybox/`.
- Room: Supabase `pes-assets/room-assets/v1.3.18/`.
- Logo 6 chế độ Rank: Supabase `pes-assets/room-assets/v1.3.40/modes/`.
- Logo CLB/giải: bucket `team-logos`.
- `modules/static_asset_service.py` là nguồn duy nhất tạo URL ảnh giao diện.
- Không tạo lại `UPLOAD_SUPABASE/` trong ZIP Production sau khi asset đã được xác minh trên Storage.

## 11. Database / Supabase

| Nhóm | Nơi kiểm tra |
|---|---|
| SQL migration mới | `migrations/` |
| SQL/docs lịch sử | `docs/*.sql` |
| Query runtime | repository/service của module sở hữu |
| Retry/query logging | `execute_query()` trong `app.py` + observability |

Không chạy SQL thay đổi dữ liệu thật trong test nếu chưa có guard/test DB rõ ràng.

---

## 12. Logging / Debug

| File | Mục đích |
|---|---|
| `Log.md` | changelog phiên bản, không phải runtime log |
| `logs/pes_arena.log` | runtime JSONL local khi bật |
| `logs/README.md` | schema và cách đọc runtime log |
| `docs/LOGGING_GUIDE_V1.3.61.md` | quy trình debug chuẩn |
| `modules/observability/app_logging.py` | logger implementation |

### Chuỗi debug chuẩn

`UI action → endpoint → request_id → service/repository → Supabase → response → UI render`

---

## 13. Test strategy

1. Test file/module đang sửa.
2. Test dependency trực tiếp.
3. `python -m py_compile` cho Python đã đổi.
4. Test source/boundary nếu có move module.
5. Full `pytest` cuối cùng; nếu baseline đã lỗi thì ghi rõ **baseline lỗi nào / lỗi mới nào**.

### Baseline V1.3.60 đã có trước V1.3.61

- `test_arena_room_cleanup_v138.py`: source test cũ đọc `room_detail.html` monolith.
- `test_room_action_visibility_v1319.py`: source test cũ đọc route name trực tiếp trong `room_detail.html`.
- `test_luckybox_core_source.py`: thiếu SQL lịch sử.
- `test_luckybox_admin_source.py`: thiếu SQL lịch sử.

Các lỗi baseline này không được tính là regression của V1.3.61.
