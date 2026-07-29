# Collap V1.14.39.7

- Thay đổi Giới hạn thi đấu Rank mỗi ngày: không còn chặn tạo phòng, mời đấu, vào phòng, Sẵn sàng hoặc Đá tiếp.
- Trận thứ 11 trở đi trong ngày thường và trận thứ 16 trở đi vào cuối tuần vẫn được chơi và lưu lịch sử.
- Trận vượt giới hạn nhận 0 RP cho cả hai, không tác động chuỗi thắng/thua và không phát danh hiệu.
- Ghi rõ lý do không tính RP trong `matches.note` và `rp_details.daily_rank_limits`.
## Collap_V1.14.39.9 — 29/07/2026
- `templates/room_detail.html` khoảng dòng 660, 790–940: polling phòng dùng endpoint partial `/api/room/<id>/view`, không tải lại toàn bộ trang; giữ node shell và chỉ thay nội dung động. Tăng nhẹ chu kỳ polling ở trạng thái ít khẩn cấp để giảm giật trên điện thoại.
- `templates/_room_live_content.html`: đồng bộ fragment với giao diện phòng hiện tại để tránh partial cũ lệch nút/form.
- `modules/room_access_routes.py` khoảng dòng 205–230: partial trả thêm state key và trạng thái qua response header.
- `templates/base.html` khoảng dòng 8–16, 950–985: CSS/JS Zcoin chỉ tải tại trang cần dùng; thông báo hệ thống đổi 15 giây thành 60 giây; lời mời giảm tần suất nhưng vẫn ưu tiên trang phòng/BXH.
- `templates/partials/room_dynamic_state.html`: bỏ tham chiếu ảnh `rank_frames/*.png` không tồn tại, tránh request 404.
- Toàn bộ template: chuẩn hóa URL ảnh `asset_url()` không gắn thêm `?v=APP_VERSION`; phiên bản tài nguyên đã nằm trong thư mục Supabase `/v1/`.
- Không thay đổi database và không cần chạy SQL.
