# V1.14.41.8

## Nội dung
- Sửa hiển thị Parsec ngay khi mở phòng.
- Đưa bảng Parsec sang cột bên phải.
- Thêm `parsec-logo.webp`, kích thước giao diện 22×22 px.
- Rút gọn tên phiên bản và hiển thị đầy đủ logo PES Arena.

## Supabase Storage
Upload file sau vào cùng thư mục public đang được `STATIC_ASSET_BASE_URL` trỏ tới:

```text
parsec-logo.webp
```

Frontend gọi bằng `asset_url('parsec-logo.webp')`. Nếu file chưa được upload hoặc biến môi trường để trống, ứng dụng sẽ dùng `/static/parsec-logo.webp`.

## SQL
Vẫn cần SQL của V1.14.41.6 nếu chưa chạy:

```text
docs/update_parsec_room_v1_14_41_6.sql
```
