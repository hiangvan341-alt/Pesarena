# Collap_V1.14.11

- `modules/room_rematch_routes.py` — khoảng dòng 25–170: cho Chủ phòng bỏ cuộc hợp lệ khi trận Rank đang `playing`; khóa theo trạng thái cũ để tránh trừ RP hai lần; mọi trận giao hữu thoát không trừ RP và không tạo lịch sử.
- `templates/room_detail.html` — khoảng dòng 429–492: sửa nút thoát giao hữu thành thoát an toàn; thêm nút bỏ cuộc cho Chủ phòng khi Rank đang thi đấu.
- `templates/_room_live_content.html` — khoảng dòng 389–452: đồng bộ nút thoát khi giao diện phòng cập nhật trực tiếp.
- `templates/partials/room_dynamic_state.html` — khoảng dòng 345–410: đồng bộ nút thoát khi polling cập nhật trạng thái phòng.
- Khác `Collap_V1.14.10`: Chủ phòng không còn bị kẹt trong trạng thái `playing`; giao hữu thường và Random 3 chọn 1 đều không còn cảnh báo/trừ 20 RP khi thoát.
