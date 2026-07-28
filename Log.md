# Collap_V1.14.34

- `templates/room_detail.html` khoảng dòng 184–188 và 744–785: sửa ô nhập tỷ số; khi giá trị là 0, bấm/focus sẽ chọn toàn bộ để số mới thay thế 0; chặn con lăn chuột làm đổi tỷ số; giới hạn 0–99; tiếp tục giữ bản nháp khi polling.
- `templates/_room_live_content.html` khoảng dòng 144–148: đồng bộ thuộc tính ô tỷ số cho giao diện cập nhật trực tiếp.
- `templates/partials/room_dynamic_state.html` khoảng dòng 423–427: đồng bộ thuộc tính ô tỷ số cho giao diện polling.
- Khác V1.14.33: nhập `4` tại ô mặc định `0` sẽ thành `4`, không còn thành `40`.
