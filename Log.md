# Collap_V1.14.29

- `modules/daily_rank_limit_service.py` (khoảng dòng 1–190): thêm hàm xác định người đã chạm giới hạn và thông báo chặn dùng chung.
- `app.py` (khoảng dòng 4570–5390): chặn tạo phòng Rank, gửi lời mời, Tìm Nhanh và nhận lời mời khi một trong hai người đã đủ số trận.
- `modules/room_access_routes.py` (khoảng dòng 20–285): chặn vào phòng qua link; cho rời phòng an toàn nếu phòng không thể bắt đầu vì giới hạn ngày; truyền trạng thái giới hạn ra giao diện.
- `modules/room_team_routes.py` (khoảng dòng 396–440): chặn Sân khách bấm Sẵn Sàng khi một trong hai người đã đủ lượt.
- `modules/room_rematch_routes.py` (khoảng dòng 1–180): ngăn route bỏ cuộc trừ 20 RP tại `waiting_ready` nếu phòng đã bị khóa bởi giới hạn ngày.
- `templates/room_detail.html`, `templates/_room_live_content.html`, `templates/partials/room_dynamic_state.html`: ẩn thao tác bắt đầu trận, hiển thị cảnh báo giới hạn và chuyển nút thoát sang luồng không trừ RP.

Khác V1.14.28: giới hạn không còn chỉ được kiểm tra lúc tạo trận; người đã đủ lượt không thể đi vào chuỗi tạo phòng → mời/nhận lời → Sẵn Sàng, nên không còn bị trừ 20 RP oan khi thoát phòng.
