# Rà soát Tìm Nhanh V1.14.41.30

## Kết luận
Cơ chế ưu tiên đang hoạt động đúng theo cấu hình đã chốt. Trước V1.14.41.30, Tìm Nhanh chưa được tách hoàn toàn: backend nằm trong `app.py`, JavaScript nằm trong `base.html`, CSS nằm cuối `style.css`. Bản này đã tách phần có thể tách an toàn thành module riêng.

## Cấu trúc mới
- `modules/quick_match/service.py`: quy tắc nhóm ưu tiên và khóa sắp xếp.
- `static/css/quick_match.css`: chỉ chứa giao diện nút và modal Tìm Nhanh.
- `static/js/quick_match.js`: gửi lời mời, theo dõi trạng thái, tự chuyển đối thủ.
- `templates/partials/quick_match_notice.html`: modal thông báo.

Route HTTP vẫn nằm trong `app.py` vì đang dùng nhiều hàm phòng, session, lời mời và Supabase của lõi dự án. Việc chuyển route sang Blueprint riêng cần một đợt refactor dependency injection lớn hơn; không nên làm chung với bản sửa giao diện vì tăng rủi ro.

## Chồng chéo CSS
- CSS Tìm Nhanh không còn nằm trong `style.css`.
- Selector đều được giới hạn bằng `.room-layout-v137 .room-quick-match-row` hoặc `.game-notice-*`.
- Các khai báo lặp trong media query là override responsive có chủ đích, không phải lệnh chồng lỗi.
- `style.css` toàn dự án vẫn có nhiều selector lịch sử được ghi đè theo phiên bản và breakpoint. Không xóa hàng loạt tự động vì có thể làm hỏng trạng thái phòng/BXH/mobile ít xuất hiện.

## Request
- Chặn request kép bằng `requestInFlight`.
- Poll trạng thái lời mời vẫn mỗi 3 giây khi có lượt đang chờ; không chạy nếu không có lượt.
- CSS/JS Tìm Nhanh chỉ tải ở trang phòng đấu.
