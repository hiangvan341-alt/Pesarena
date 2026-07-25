# Collap_V1.14.2

- `app.py` khoảng dòng 65, 591–600 và 4530–4545.
- Bổ sung `public_ranking_enabled` vào cấu hình tính năng hệ thống để công tắc Admin được lưu đúng.
- Khi Admin tắt **BXH công khai**, khách chưa đăng nhập truy cập `/`, `/ranking` hoặc `/bxh` sẽ được chuyển tới trang đăng nhập và nhận thông báo.
- Người đã đăng nhập vẫn xem BXH bình thường.
- Giữ nguyên API, RP, phòng đấu, animation và polling của `Collap_V1.14.1`.
