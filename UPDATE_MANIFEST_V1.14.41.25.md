# V1.14.41.25

Ngày: 31/07/2026 01:43 (Asia/Bangkok)

## Sửa Tìm Nhanh

- Không dùng `list_players()` có cache để phát hiện đối thủ online.
- Đọc trực tiếp `users.last_seen_at` từ Supabase khi bấm Tìm Nhanh.
- Dùng cửa sổ presence 90 giây để tránh bỏ sót heartbeat giữa các instance Vercel.
- Chỉ lấy tài khoản `role=player`, `account_status=approved`.
- Giữ nguyên các lớp loại trừ: đang thi đấu, có lời mời, phòng đã đủ người, cooldown.
- Thay thông báo `window.alert()` bằng modal PES Arena đồng bộ giao diện.

## File thay đổi

- `app.py`
- `templates/base.html`
- `static/style.css`
- `Log.md`
