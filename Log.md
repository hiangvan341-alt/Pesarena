## V1.14.41.39 — 31/07/2026 11:25 (Asia/Bangkok)


## V1.14.41.51 — Sửa xóa tài khoản làm tụt RP — 02/08/2026 01:32 (Asia/Bangkok)

- Sửa `modules/data_cleanup_service.py`: xóa tài khoản không còn hoàn tác RP/thống kê của các đối thủ từng thi đấu.
- Chặn xử lý trùng một trận khi trận vừa nằm trong phòng vừa nằm trong danh sách trận cache.
- Giữ nguyên hành vi hoàn tác RP khi Admin chủ động xóa phòng/trận riêng lẻ.
- Thêm kiểm tra nguồn `TEST_DELETE_PLAYER_RP_V1.14.41.51.py`.

- Sửa lỗi số phiên bản trên giao diện bị giữ ở `V1.14.41.36`.
- Nguyên nhân: các bản 37 và 38 không cập nhật hằng số `APP_VERSION` trong `app.py`.
- Cập nhật `APP_VERSION` thành `V1.14.41.39`.

## V1.14.41.40
- Rà soát request/polling, dữ liệu trùng và file tải thừa.
- Chỉ tải zcoin_rewards CSS/JS tại endpoint tương ứng.
- Room state dừng khi tab ẩn; pending invite dùng chu kỳ 2,2s/8s.
- Xóa module/template Zcoin cũ không còn dùng.
- Bỏ reload bảo trì 30 giây bị trùng.


## V1.14.41.50 — Tối ưu ảnh — 02/08/2026 01:28 (Asia/Bangkok)
- Rà soát toàn bộ ảnh trong dự án.
- Xóa ảnh local đã có trong `SUPABASE_ASSET_MANIFEST.csv`.
- Xóa PNG cũ/trùng WebP và ảnh kiểm thử không dùng.
- Sửa `static/style.css` để nền đăng nhập chỉ lấy qua `asset_url()`/Supabase.
- Thêm `IMAGE_OPTIMIZATION_V1.14.41.50.md`.


## V1.14.41.52 — Xóa mềm tài khoản và bảo vệ thao tác kích khách — 02/08/2026 01:43 (Asia/Bangkok)

- Đổi xóa tài khoản sang xóa mềm: giữ nguyên dòng `users`, toàn bộ `matches`, phòng đã có `match_id`, tỷ số và RP lịch sử.
- Vô hiệu hóa đăng nhập bằng `account_status=banned`, đặt mật khẩu ngẫu nhiên và trạng thái Offline.
- Chỉ dọn phòng chờ chưa có trận, thiết bị đăng nhập và lời mời chưa hoàn tất.
- Sửa nút Admin thành “Xóa mềm” và cảnh báo rõ lịch sử/RP được giữ nguyên.
- Rà cơ chế chủ phòng kích khách: chỉ cho phép trước khi bắt đầu; chặn thêm khi đã có `match_id`.
- Khi kích khách, đóng lời mời liên kết để không còn trạng thái lời mời treo; không xóa trận và không thay đổi RP.
