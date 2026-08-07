# PES Arena V1.3.34 — Read Model / Stats Cache Audit

## Mục tiêu

Loại bỏ kiểu xử lý **click tab -> tải toàn bộ dữ liệu -> Python tính toán lại** ở các màn hình được xem thường xuyên.

## Đã chuyển sang dữ liệu tính sẵn trong Supabase

### Admin → Báo cáo số trận
Trước V1.3.34, khi mở báo cáo server phải đọc `matches`, `match_rooms`, `match_series`, `match_series_games`, parse `rp_details/note`, đếm theo ngày/chế độ, tính RP/series/comeback và duyệt user để đếm mở khóa.

V1.3.34 dùng các read model:
- `admin_match_daily_stats`
- `admin_match_mode_daily_stats`
- `admin_match_player_daily_stats`
- `admin_series_daily_stats`
- `admin_rank_mode_unlock_stats`

Request mở tab chỉ SELECT các bảng nhỏ này. Nếu migration chưa chạy, hệ thống **không fallback quét lịch sử**, mà báo cần chạy SQL để tránh treo request.

### BXH → phong độ 5 trận
Dùng `player_recent_form_cache`. Trigger cập nhật sau khi trận thay đổi. BXH không còn gọi `list_matches(status="confirmed")`.

### Hồ sơ người chơi
- `player_profile_stats_cache`: đội dùng nhiều nhất + đối thủ gặp nhiều nhất.
- `player_pair_stats_cache`: H2H tổng hợp.
- Trận gần đây dùng query đúng user, có `LIMIT`, không `list_matches()` toàn hệ thống.

### Dashboard
Trận gần đây và trạng thái cần chú ý lấy đúng trận của user bằng query có điều kiện, không tải toàn bộ lịch sử.

### Admin → IP trùng
`admin_user_ip_summary_cache` và `admin_duplicate_ip_cache` được cập nhật khi quan hệ user/IP thay đổi. Mở Admin không cần đọc và group toàn bộ `user_devices` nữa.

## Dữ liệu vẫn để realtime
Các dữ liệu sau không nên cache dài hạn vì bản chất thay đổi liên tục:
- Online/offline.
- Phòng đang hoạt động.
- Countdown.
- Lời mời pending.
- Trạng thái trận hiện tại.

Các phần này nên query đúng bản ghi cần thiết và không chạy aggregation lịch sử.

## Cách triển khai
1. Chạy `SUPABASE_UPDATE_V1.3.34.sql` trong Supabase SQL Editor.
2. Chờ SQL backfill hoàn tất.
3. Deploy source V1.3.34 lên Vercel.
4. Vào Admin → Báo cáo số trận và thử các mốc thời gian.
5. Kiểm tra Vercel Logs: `ADMIN_PERF` không còn `report_matches` lớn; báo cáo dùng `source=read_model`.

## Lưu ý
Migration tạo trigger cập nhật read model tại thời điểm dữ liệu gốc thay đổi. Vì vậy chi phí được chuyển khỏi request người dùng; click tab chỉ đọc dữ liệu đã chuẩn bị sẵn.
