# V1.14.41.13 — Chuẩn hóa giao diện module Parsec

- Làm lại riêng module Parsec theo ảnh mẫu; không thay đổi các khung phòng đấu khác.
- Khóa logo Parsec 18 × 18 px trong đúng file CSS của module.
- Xóa CSS bảo vệ logo bị lặp trong `static/style.css` và bỏ toàn bộ inline CSS trên ảnh logo.
- Nút Copy ID chuyển về nền xanh đen, viền vàng mảnh; nút Copy Link giữ màu hồng theo ảnh mẫu.
- Đồng bộ font Inter/Segoe UI/Arial trong toàn bộ module và cho button/input/select/textarea kế thừa font chung.
- Sắp xếp cột phải cố định: Thông tin phòng → Parsec → Lịch sử đấu → Chat.
- Giữ nguyên phân quyền chủ phòng/khách và toàn bộ logic lưu, xóa, sao chép Parsec.

