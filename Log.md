# Collap_V1.14.35_ZCOIN_PHASE1_CLEAN

- Baseline: `Collap_V1.14.34`.
- Giữ nguyên toàn bộ sửa lỗi nhập tỷ số của V1.14.34.
- Khôi phục Zcoin Giai đoạn 1 trên source mới: số dư topbar, menu tài khoản, Ví Zcoin, lịch sử giao dịch và quản trị cộng/trừ Zcoin.
- Dùng đúng schema Zcoin đã tồn tại; không tạo lại bảng và không reset dữ liệu.
- Thay logo Zcoin trong V1.14.34 bằng logo vàng chữ Z chính thức.
- Tinh gọn trang Ví: bỏ khung “Giai đoạn 1”, roadmap nội bộ và các mô tả lặp.
- Database đã chạy RPC tương thích ở V1.14.33 không cần chạy lại SQL.

# Collap_V1.14.34

- `templates/room_detail.html`: sửa ô nhập tỷ số; khi giá trị là 0, bấm/focus sẽ chọn toàn bộ để số mới thay thế 0; chặn con lăn chuột làm đổi tỷ số; giới hạn 0–99; tiếp tục giữ bản nháp khi polling.
- `templates/_room_live_content.html`: đồng bộ thuộc tính ô tỷ số cho giao diện cập nhật trực tiếp.
- `templates/partials/room_dynamic_state.html`: đồng bộ thuộc tính ô tỷ số cho giao diện polling.
- Khác V1.14.33: nhập `4` tại ô mặc định `0` sẽ thành `4`, không còn thành `40`.
