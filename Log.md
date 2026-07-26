# Collap_V1.14.12

- `modules/room_team_routes.py` khoảng dòng 134–235: chuyển Random 3 chọn 1 từ giao hữu sang trận xếp hạng; tạo match khi hai bên chọn xong và gắn vào luồng tính RP.
- `modules/admin_system_routes.py` khoảng dòng 105–125: khi Admin tắt Random 3 chọn 1 chỉ hủy lượt chọn chưa bắt đầu; trận RP đang thi đấu vẫn được hoàn tất.
- `app.py` khoảng dòng 2810: giữ nhãn Random 3 chọn 1 trong suốt trận đấu.
- `templates/room_detail.html`, `templates/_room_live_content.html`, `templates/partials/room_dynamic_state.html`: cập nhật mô tả thành tính RP và lưu lịch sử.
- Khác V1.14.11: Random 3 chọn 1 không còn là giao hữu; kết quả đi qua nhập kết quả, xác nhận, tranh chấp, lịch sử và công thức RP hiện tại.
