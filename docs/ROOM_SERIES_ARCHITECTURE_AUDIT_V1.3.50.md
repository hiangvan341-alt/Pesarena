# PES Arena V1.3.50 — Room / Rank Mode / Series architecture audit

## 1. Hai lỗi người dùng báo và nguyên nhân gốc

### A. Vào phòng đấu rất chậm
Luồng V1.3.49 khi render phòng gọi `rank_mode_catalog_for_players()` cho 6 mode. Mỗi mode lại gọi daily quota cho host/guest; `rank_daily_status()` tiếp tục đọc setting và bảng matches nhiều lần. Trong cold request có thể phát sinh hàng chục SELECT chỉ để dựng danh sách 6 mode. API polling `/api/room/<id>/state` còn dùng `get_room()`, tức chạy toàn bộ `enrich_room()` (users map, team hydrate, cosmetics...) dù client chỉ cần state key.

V1.3.50 sửa:
- cache rank-mode config theo request + TTL 8 giây;
- daily-rank config/matches cache theo request + TTL setting;
- catalog tải daily status đúng 1 lần/player rồi dùng lại cho cả 6 mode;
- polling dùng `get_room_poll_snapshot()` không chạy `enrich_room()`;
- polling Series thêm `get_series_poll_version()` để nhận thay đổi chọn/cấm đội mà không cần full hydration.

### B. Admin chỉ bật Lượt đi/về nhưng phòng vẫn hiện Rank thường
V1.3.49 dùng:
`SMART_RANDOM_MODE if rank_standard_enabled else random3_pick1`

Nhưng `rank_standard_enabled` đã được Admin route định nghĩa là **có ít nhất một chế độ Rank đang bật**, không phải **Rank thường đang bật**. Vì vậy chỉ bật `home_away` vẫn làm biểu thức chọn `smart_random`.

Ngoài ra `enrich_room()` còn có fallback ép room sang `random3_pick1` khi cờ legacy tắt. Đây là hai nguồn sự thật xung đột.

V1.3.50 sửa thành một nguồn chuẩn:
`rank_mode_configs_v1 -> default_rank_mode_code() -> default_rank_room_team_tier()`.

Các luồng tạo phòng mở, tạo phòng khi gửi invite và tạo phòng khi accept invite đều dùng resolver này. Phòng waiting cũ nếu đang giữ mode đã bị Admin khóa sẽ được migrate có điều kiện khi mở phòng; Series đang hoạt động không bị đổi mode giữa chừng.

## 2. Luồng chuẩn mới

Admin System -> `rank_mode_configs_v1.enabled`
-> `get_rank_mode_configs()` (request/TTL cache)
-> `default_rank_mode_code()` / `resolve_enabled_rank_mode()`
-> `match_rooms.team_tier`
-> `build_room_template_context()`
-> UI mode/logo/action
-> nếu Series: `modules/rank_series/service.py`
-> `match_series`
-> `match_series_games`
-> child `matches`
-> confirm child delta 0
-> resolve Series
-> apply RP đúng một lần ở child cuối.

## 3. Audit 4 lõi Series

| Mode | Tạo trận con | Tiếp trận 2/3 | RP một lần | Auto confirm | Tranh chấp | Bỏ cuộc | Polling đối thủ |
|---|---|---|---|---|---|---|---|
| Home/Away | OK | OK, 2 lượt | OK | FIX 1.3.50 | FIX 1.3.50 | OK | FIX 1.3.50 |
| BO3 | OK | OK đến đủ 2 win / max 3 | OK | FIX 1.3.50 | FIX 1.3.50 | OK | FIX 1.3.50 |
| Tactical BO3 | 3 lựa chọn riêng/player | OK | OK | FIX 1.3.50 | FIX 1.3.50 | OK | FIX 1.3.50 |
| Ban/Pick BO3 | pool chung, 6 ban, pick | OK | OK | FIX 1.3.50 | FIX 1.3.50 | OK | FIX 1.3.50 |

### Hai lỗi lõi Series tìm thấy thêm
1. Auto-confirm 60 giây trước đây đi qua `apply_match_result()` của trận đơn, có nguy cơ cộng RP theo từng child và không hoàn tất `match_series_games`. Nay dispatch sang `confirm_series_child_match()`.
2. Tranh chấp child trước đây giải phóng room nhưng để Series/game child ở trạng thái active. Nay hủy Series + đóng child game chưa hoàn tất để không tạo Series mồ côi/duplicate game.

## 4. State/polling
`build_room_state_key()` nay có `match_mode`, `team_tier`, `updated_at` và `series_version`.
Điều này sửa hai lỗi realtime:
- Admin/room đổi mode nhưng UI không refresh vì state key cũ không chứa mode;
- Tactical/Ban-Pick thay đổi metadata của `match_series` nhưng room row không đổi, khiến đối thủ không thấy lượt mới.

## 5. Phần chưa tự động hóa
`ban_seconds` và `pick_seconds` đang là cấu hình thời gian trong catalog nhưng chưa có luật **auto-ban/auto-pick khi hết giờ**. Luồng cấm/chọn thủ công hoạt động; không tự tạo hành vi ngẫu nhiên vì chưa có quy tắc sản phẩm được chốt cho trường hợp hết giờ.

## 6. Test
Bộ test tập trung V1.3.50 + Series: 45 PASS.
Bao phủ: mode resolver, room creation source, lightweight polling, Series version key, daily quota N+1 guard, second-game routing, Series auto-confirm, dispute cleanup, RP one-time, forfeit, module boundary/CSS structure.
