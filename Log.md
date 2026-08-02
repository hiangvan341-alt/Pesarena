## V1.14.41.58 — 2026-08-02 07:45 (Asia/Bangkok)

- Thêm thưởng RP hoạt động tuần theo số trận và số đối thủ khác nhau.
- Mỗi mốc chỉ nhận một lần/tuần bằng bảng `weekly_rp_rewards`.
- Mốc thưởng cộng dồn: 10 trận +20; 5 đối thủ +30; 10 đối thủ +50; 20 đối thủ +50 RP.
- Chỉ trận confirmed được xét thưởng; tranh chấp chỉ được xét sau khi Admin xác nhận.
- Thêm SQL `docs/update_weekly_rp_rewards_v1_14_41_58.sql`.

## V1.14.41.57 — 2026-08-02 07:17 (Asia/Bangkok)

- Đổi thời gian chờ xác nhận kết quả Rank từ 12 giờ xuống 1 phút.
- Hết 1 phút không xác nhận hoặc tranh chấp, hệ thống tự xác nhận và cộng/trừ RP.
- Luồng phòng và luồng kết quả tiếp tục độc lập: hủy phòng không hủy kết quả đang chờ.
- Trận có tranh chấp không tự xác nhận, chờ Admin xử lý.

## V1.14.41.53 — Bảo vệ Hủy/Xóa phòng Admin — 02/08/2026 01:47 (Asia/Bangkok)
- Khách đã Sẵn sàng vẫn có thể bị chủ phòng đưa ra nếu phòng chưa tạo trận (`waiting_ready`, không có `match_id`); không ảnh hưởng RP.
- Admin Hủy phòng giữ lịch sử phòng/trận, hoàn tác RP trước khi cập nhật trạng thái và hủy lời mời liên kết.
- Admin chỉ được xóa vật lý phòng chờ chưa có trận; phòng có trận bắt buộc dùng Hủy.
- File: `app.py`, `modules/admin_data_routes.py`, `templates/admin.html`.

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

## V1.14.41.54 — 02/08/2026 01:53 (Asia/Bangkok)
- Bỏ hoàn toàn chức năng Admin xóa phòng; giao diện chỉ còn nút **Hủy phòng**.
- Hủy phòng chỉ giải phóng người chơi để tạo phòng mới, không hoàn tác hoặc thay đổi RP.
- Hỗ trợ phòng một người, chưa có trận, đang chơi, đã có kết quả, chờ xác nhận, tranh chấp và có báo cáo.
- Giữ nguyên lịch sử, tỷ số, delta RP, báo cáo và bằng chứng tranh chấp.
- Trận chưa hoàn tất chuyển `cancelled` để không khóa người chơi; trận đã `confirmed` giữ nguyên.
- File: `app.py`, `modules/admin_data_routes.py`, `templates/admin.html`.

## V1.14.41.55 - 02/08/2026
- Tách trạng thái tranh chấp khỏi trạng thái phòng.
- Trận bị tranh chấp vẫn lưu và chưa tính RP; phòng lập tức trở lại Chờ Sẵn Sàng.
- Người chơi có thể tiếp tục thi đấu trong cùng phòng mà không chờ Admin xử lý tranh chấp cũ.
- File: `modules/room_result_routes.py`, `app.py`.


## V1.14.41.56 — 2026-08-02 07:12 (Asia/Bangkok)
- Tách hủy phòng khỏi xử lý kết quả.
- Tự xác nhận trận chờ sau 12 giờ, không phạt người quên xác nhận.
- Khóa xác nhận trực tiếp trận disputed.

## V1.14.41.59 — 02/08/2026 08:08 (UTC+7)
- Điều chỉnh mốc thưởng tuần mặc định thành 20 + 30 + 50 + 20 = tối đa 120 RP.
- Bổ sung cấu hình thưởng tuần trong Admin > Hệ thống.
- File sửa: `modules/weekly_rp_rewards_service.py`, `modules/admin_system_routes.py`, `templates/admin.html`, `app.py`.

## V1.14.41.60 - 2026-08-02
- Sửa animation Win Streak và SHUTDOWN không xuất hiện khi trận được tự xác nhận sau 1 phút.
- File: app.py, UPDATE_MANIFEST_V1.14.41.60.md.

## V1.14.41.62 — 02/08/2026 09:24 (Asia/Bangkok)
- Sửa Remember this account: dùng phiên đăng nhập 30 ngày và Password Manager của trình duyệt.
- Tài khoản Admin tạo/import được dùng mật khẩu 1 ký tự.
- Tài khoản Admin tạo/import bỏ giới hạn thiết bị và cảnh báo trùng IP, nhưng vẫn tính RP bình thường.
- File: `app.py`, `modules/admin_account_routes.py`, `templates/admin.html`, `templates/login.html`.

## V1.14.41.65 — 2026-08-02 18:19 (Asia/Bangkok)
- Hoàn thiện bảo vệ phiên: truy vấn trực tiếp phòng theo user và trạng thái cần bảo vệ, không phụ thuộc cache `list_rooms()`.
- Đồng nhất trạng thái `playing`, `friendly_playing`, `waiting_result_confirm`, `waiting_confirm`, `disputed`.
- Không đăng xuất khi một phía vừa mất kết nối nhưng phòng vẫn cần hoàn tất.
- Admin hiển thị trạng thái tải `user_devices`, số bản ghi, số tài khoản có IP, số nhóm trùng và nút tải lại.
- Đổi nhãn Remember thành “Ghi nhớ đăng nhập trên thiết bị này”; làm rõ mật khẩu do trình duyệt lưu.
- Cập nhật kiểm thử: 94/94 đạt.
- File chính: `app.py`, `modules/session_runtime_service.py`, `modules/admin_dashboard_routes.py`, `templates/admin.html`, `templates/login.html`.

## V1.14.41.66 — 2026-08-02 19:30 (Asia/Bangkok)

- Sửa lỗi khách đã vào phòng nhưng phía chủ phòng không nhìn thấy.
- Bổ sung `host_user_id` và `guest_user_id` vào khóa trạng thái phòng để API phát hiện thay đổi thành viên và frontend tự tải lại phần phòng đấu.
- Không tạo thêm polling hoặc request nền.
- File: `app.py`, `test_room_guest_visibility_v1144166.py`, các test phiên bản, `UPDATE_MANIFEST_V1.14.41.66.md`.

## V1.14.41.67 — 02/08/2026 22:16 (GMT+7)

- Kiểm tra giới hạn trận Rank theo ngày Việt Nam: Thứ Hai–Thứ Sáu 10 trận, Thứ Bảy–Chủ Nhật 15 trận; đổi mốc chính xác lúc 00:00 GMT+7.
- Sửa `active_room_for_user()` truy vấn nhầm bảng `rooms`; nay truy vấn trực tiếp `match_rooms`.
- Bổ sung `waiting_ready` vào nhóm phòng active để người đang có phòng chờ không thể tạo thêm phòng mới.
- Chống double-click và request đồng thời trên nhiều Vercel instance: sau khi tạo phòng sẽ đối chiếu lại và chỉ giữ một phòng hợp lệ.
- Tự dọn các phòng `waiting_ready` trùng, chỉ xóa phòng chưa có `match_id`; không ảnh hưởng trận đang đá, kết quả, RP hoặc tranh chấp.
- Khi Admin mở trang quản trị, hệ thống tự dọn các phòng chờ trùng cũ và tải lại danh sách.
- Hủy lời mời pending gắn với phòng trùng đã bị xóa để tránh trạng thái lời mời treo.
- Kiểm tra tự động: 101/101 test đạt.

### File thay đổi
- `app.py`
- `modules/admin_dashboard_routes.py`
- `test_v1144167_room_daily_limit.py`
- `Log.md`
