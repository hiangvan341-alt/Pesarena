# V1.14.41.26 — Admin Presence Mode

Thời gian: 2026-07-31 01:46 (Asia/Bangkok)

## Nội dung
- Chỉ tài khoản Admin/Owner được chọn trạng thái hiển thị Online hoặc Offline.
- Thêm bộ chọn trạng thái trên thanh trên cùng.
- Khi Admin chọn Offline, heartbeat vẫn duy trì phiên đăng nhập nhưng không tự bật lại Online.
- Người chơi thường vẫn dùng cơ chế Online/Offline tự động như trước.
- Không cần chạy SQL mới.

## File sửa
- `app.py`
- `modules/admin_player_routes.py`
- `templates/base.html`
- `static/style.css`
- `Log.md`
