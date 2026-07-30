# V1.14.41.30 — Tách module Tìm Nhanh và dọn CSS/JS

## Thay đổi
- Tách quy tắc ưu tiên đối thủ sang `modules/quick_match/service.py`.
- Tách toàn bộ giao diện Tìm Nhanh khỏi `static/style.css` sang `static/css/quick_match.css`.
- Tách JavaScript gửi lời mời, theo dõi phản hồi và chuyển đối thủ sang `static/js/quick_match.js`.
- Tách HTML modal thông báo sang `templates/partials/quick_match_notice.html`.
- CSS/JS Tìm Nhanh chỉ tải tại trang `room_detail`, không tải ở các trang khác.
- Thêm khóa `requestInFlight` để tránh bấm nhanh tạo hai request gửi lời mời đồng thời.
- Giữ nguyên thứ tự ưu tiên: cùng Rank → ≤300 → 301–500 → 501–1000 → 1001–2000 RP.
- Cập nhật test để kiểm tra trực tiếp module thay vì dò chuỗi trong `app.py`.

## Kiểm tra
- Python compile: thành công.
- Pytest: 35/35 thành công.
- Không còn CSS hoặc JavaScript Tìm Nhanh nằm trong file dùng chung `style.css`/`base.html`.
