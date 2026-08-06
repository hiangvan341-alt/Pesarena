
## V1.3.23 — Làm sáng và đồng bộ nút phòng đấu
- Kiểm tra xung đột giữa `static/style.css` và `static/css/arena_room_v2.css`.
- Tăng độ sáng nền cho 4 nhóm nút: gold, success, secondary và danger.
- Ép chữ nút màu trắng, tăng độ đậm và thêm text-shadow nhẹ.
- Giảm mức làm tối của nút disabled để nội dung vẫn đọc được.
- Loại bỏ lớp nền phụ bên trong nút Quay quân để tránh nút hai lớp.
- Không thay đổi nút thuộc khu Parsec.
- Không thay đổi API, route hoặc logic phòng đấu.
# PES Arena V1.3.21 — Unified Room Buttons

- Đồng bộ nút phòng đấu theo một hệ thiết kế bo góc navy/neon.
- 4 biến thể: gold, success, secondary, danger.
- Áp dụng cho Mời đấu, Tìm nhanh, Sẵn sàng, Hủy sẵn sàng, Thoát phòng, Gửi kết quả, xác nhận, từ chối, Quay quân, đá tiếp và điều khiển phòng.
- Không áp dụng cho nút trong khu vực Parsec.
- Giữ nguyên route, API, JavaScript và logic phòng đấu.

## V1.3.18 - 2026-08-07

- Dùng `room-texture-dark.webp` làm nền toàn bộ khu phòng đấu.
- Bỏ nền mờ/đục ở card chế độ; thay bằng viền Neon tím, xanh và gold.
- Tăng kích thước emblem chế độ trung tâm và icon của 6 chế độ.
- Chuyển URL Supabase mặc định sang `pes-assets/room-assets/v1.3.18`.
- Không thay đổi API, polling hoặc luồng phòng đấu.

## V1.3.17 - 2026-08-07

- Bỏ hoàn toàn `light-effect-blue.webp` và `light-effect-red.webp` khỏi CSS, template, asset local và gói upload Supabase.
- Card Chủ phòng/Đối thủ chỉ dùng trực tiếp `stadium-blue.webp` và `stadium-red.webp`, không còn request 404 hoặc lớp đèn chồng ảnh.
- Cắt vùng trong suốt dư của `pes-arena-room-logo.webp` và tăng kích thước hiển thị cân đối trên thanh tiêu đề phòng đấu.
- Chuyển đường dẫn Supabase mặc định sang `pes-assets/room-assets/v1.3.17` để tránh cache ảnh cũ.

## V1.3.16 - 2026-08-07
- Bỏ đường kẻ ngang legacy trong card Chủ phòng/Đối thủ (`border-bottom` của `.room-player-heading-plain`).
- Thay nền khu VS bằng WebP sân ngang mới và giảm lớp phủ tối để ảnh hiện rõ.
- Thay texture nền khu chế độ bằng WebP người dùng cung cấp.
- Đổi đường dẫn Supabase sang `pes-assets/room-assets/v1.3.16` để tránh cache bản cũ.
- Không đổi API, route, polling hoặc luồng sẵn sàng/thoát phòng.

# PES Arena V1.3.14

- Thay thanh “CHỌN 1 TRONG 3” bằng chữ HTML và CSS thuần.
- Cấu trúc: đường kẻ vàng, hình thoi, tiêu đề, hình thoi, đường kẻ vàng.
- Chỉ hiển thị trong chế độ `random3_pick1`.
- Áp dụng đồng bộ cho Host/Opponent và các template cập nhật động.
- CSS được giới hạn trong namespace `.arena-room-v2`.
- Không thay đổi API, JavaScript, polling hoặc logic phòng đấu.
- Không cần SQL và không cần upload thêm ảnh Supabase.

# PES Arena V1.3.6 — Room UI Asset Pack

- Ngày: 2026-08-06 22:45 (Asia/Bangkok)
- Dựa trên: V1.3.5 Arena Room V2 UI MASTER.
- Tạo đủ asset WebP: logo phòng đấu, nền sân xanh/đỏ, light effect xanh/đỏ, VS emblem, Parsec, chia sẻ phòng, 6 icon chế độ.
- Viết lại CSS phòng đấu dưới namespace `.arena-room-v2`: layout, card, nút, typography, grid, spacing, badge, Tổng điểm và hệ thống khung neon.
- Giữ nguyên API, form, polling, sidebar, header và các module ngoài phòng đấu.
- Asset có thể dùng local ngay; chuẩn bị sẵn cấu trúc để tải lên Supabase Storage.

# PES Arena V1.3.5 — Arena Room V2

- Ngày: 2026-08-06 (Asia/Bangkok)
- Dựng lại riêng khu vực phòng đấu theo UI MASTER, không tiếp tục vá layout cũ.
- Root namespace mới: `.arena-room-v2`.
- Viết lại bố cục chính bằng CSS Grid 4 cột: 31% / 24% / 31% / 14%.
- Giữ nguyên Sidebar, Header chung, API, form action, dữ liệu Jinja và JavaScript phòng đấu hiện có.
- Ba nút hành động được trình bày ngang trong khu trung tâm ở trạng thái chờ đối thủ.
- Sáu card chế độ nằm cùng một hàng desktop; giữ đúng tên “Cấm chọn CLB”.
- Thay emoji chế độ chính bằng 6 SVG riêng trong `static/icons/rank_modes/`.
- Không dùng OVR, inline style, selector chung hoặc `!important`.
- File CSS mới: `static/css/arena_room_v2.css`.
- Không có SQL mới. SQL mới nhất vẫn nằm tại `docs/PES_ARENA_UPDATE_LATEST.sql`.

## File sửa

- `app.py`
- `templates/room_detail.html`
- `static/css/arena_room_v2.css`
- `static/icons/rank_modes/*.svg`
- `test_arena_room_v2_v135.py`

---

# PES Arena V1.3.4 — Fix UI MASTER 100%

- Sửa `room-arena-frame` còn kế thừa `min-height: 720px` từ CSS cũ.
- Khung thi đấu desktop còn 405px và dải 6 chế độ luôn nằm ngay phía dưới ở zoom 100%.
- Thu gọn topbar riêng trang `room_detail`, không ảnh hưởng trang khác.
- Không dùng CSS zoom/transform scale, không thêm polling hoặc JavaScript.
- CSS mới chỉ nằm trong `body[data-page="room_detail"]` và `.room-layout-v137`.
- Không cần chạy SQL mới.

## V1.3.1 — 06/08/2026 21:47 (GMT+7)
- Thêm tab `Quản lý chế độ Rank` trong Dashboard Admin cho đủ 6 chế độ.
- Cho phép lưu bật/tắt, RP mở khóa, số trận tối thiểu, chênh RP tối đa và bảng RP Series vào `system_settings`.
- Bổ sung cấu hình Pool CLB, lượt cấm, thời gian cấm và thời gian chọn cho Cấm chọn CLB BO3.
- Mở rộng báo cáo đủ 6 chế độ: trận, Series, hoàn thành, 2-0, 2-1, hòa, bỏ cuộc, tranh chấp, RP cộng/trừ, RP trung bình, lội ngược dòng và số người đã mở khóa.
- Tương thích dữ liệu trận cũ; nếu bảng Series chưa được tạo, trang Admin vẫn hoạt động và hiển thị số liệu Series bằng 0.
- File sửa: `app.py`, `modules/rank_modes/service.py`, `modules/admin_dashboard_routes.py`, `templates/admin.html`, `static/css/admin_dashboard.css`, `Log.md`.

## V1.2.6 — 05/08/2026 00:47 (GMT+7)
- Sửa lỗi tài khoản vẫn bị báo còn trận chưa hoàn tất dù phòng đã bị đóng hoặc không còn tồn tại.
- Chỉ khóa tạo phòng khi bản ghi trận còn liên kết với một phòng đang hoạt động.
- Bỏ qua các trận mồ côi có trạng thái `playing`/`waiting_confirm` nhưng phòng đã `cancelled` hoặc đã mất.
- Đồng bộ xóa cache trận sau khi ghi nhận bỏ cuộc do chủ phòng Offline.
- File sửa: `app.py`, `modules/forfeit_history_service.py`.

## V1.2.5 — 05/08/2026 00:43 (GMT+7)
- Admin hiển thị riêng các phòng đã tự đóng do chủ phòng Offline.
- Phòng đã đóng không còn khóa người chơi nhưng vẫn lưu để Admin xem chủ, khách, đội, lý do và chi tiết phòng.
- Bổ sung đầy đủ trạng thái phòng đang hoạt động trong tab quản trị.
- File sửa: `app.py`, `modules/admin_dashboard_routes.py`, `templates/admin.html`.

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


## V1.14.41.68 — 02/08/2026 23:35 (GMT+7)
- Sửa công thức thưởng chuỗi: chỉ RP thắng cơ bản chịu hệ số gặp lại và hệ số chủ phòng.
- Thưởng chuỗi được cộng nguyên vẹn.
- Đồng bộ luồng xác nhận trận và tính lại BXH Admin.
- Thêm test riêng cho thắng lần 3 cùng đối thủ khi chạm chuỗi 10.

## V1.14.41.73–77 — Profile V2
- Làm mới trang hồ sơ theo bố cục Champion Showcase / Arena Overview.
- Banner phủ khung, có lớp gradient; avatar, RP, Rank, huy hiệu và hành trình Rank rõ hơn.
- Hồ sơ chưa trang bị banner không còn hiện cụm chữ lớn mặc định.
- Không thay đổi SQL hoặc logic thi đấu.

## V1.14.41.78 — Room Session Guard
- Bảo vệ phòng đang thi đấu tối đa 4 giờ khi người chơi chuyển sang PES/Parsec.
- Request trang/API phòng được tính là hoạt động trước bộ lọc idle.
- Tab nền tiếp tục đồng bộ phiên; người ngoài phòng vẫn timeout sau 60 phút.

## V1.14.41.79 — Result Confirmation Reliability
- Sửa lỗi `NameError: get_win_streak_bonus is not defined` khi khách xác nhận tỷ số.
- `match_result_service.py` import trực tiếp `random` và `get_win_streak_bonus`.
- Giữ nguyên công thức RP, giới hạn ngày, hệ số gặp lại và session guard V1.14.41.78.

## V1.14.41.79 Clean — 04/08/2026 01:42 (Asia/Bangkok)
- Xóa toàn bộ Markdown thừa, chỉ giữ `Log.md`.
- Xóa cache Python/Pytest và các manifest TXT cũ.
- Xóa ảnh local đã có trong `SUPABASE_ASSET_MANIFEST.csv` cùng PNG/test image trùng hoặc không dùng.
- ZIP không bọc thư mục cha; yêu cầu cấu hình `STATIC_ASSET_BASE_URL` và `SHOP_ASSET_BASE_URL` trên Vercel.


## V1.14.41.80 — 04/08/2026 01:55 (GMT+7)
- Hòa đặt chuỗi thắng về 0; đồng bộ cả luồng xác nhận trực tiếp và tính lại BXH Admin.
- Đối thủ bỏ cuộc: người còn lại được +1 trận thắng và +1 chuỗi thắng, nhưng +0 RP.
- Giữ tự động xác nhận sau 60 giây và hiển thị đồng hồ đếm ngược ngay dưới tỷ số.
- File sửa: `app.py`, `modules/match_result_service.py`, `modules/admin_ranking_rebuild.py`, `modules/room_rematch_routes.py`, 3 template phòng, `static/style.css`.


## V1.2.0 — 04/08/2026 02:00 (GMT+7)

- Nâng phiên bản chính lên V1.2.0.
- Kiểm tra và gia cố toàn bộ luồng nhập/xác nhận tỷ số.
- Không cho polling thay khung phòng khi chủ phòng đang nhập tỷ số.
- Kiểm tra tỷ số 0–99 ở cả trình duyệt và máy chủ; không tự đổi ô trống thành 0.
- Giữ bản nháp tỷ số khi lỗi mạng.
- Chống trạng thái dở dang khi match đã lưu nhưng phòng chưa đổi trạng thái; tự hoàn tác an toàn.
- Mỗi lỗi lưu/xác nhận có mã riêng SCORE/CONFIRM/ROOM để tra log.
- Phân biệt rõ trường hợp RP đã ghi nhận nhưng phòng chưa làm mới.
- Lỗi phụ của animation chuỗi thắng không còn chặn xác nhận kết quả.

## V1.2.1 — 04/08/2026 02:26 (GMT+7)
- Tự động tạo fingerprint theo nội dung cho CSS/JS, không còn phụ thuộc hoàn toàn vào việc đổi phiên bản để phá cache.
- Tách CSS Thưởng RP tuần thành module riêng, giới hạn phạm vi trong trang Admin và loại bỏ CSS trùng/inline của module này.
- Thêm công cụ `scripts/bump_version.py` và `scripts/check_ui_assets.py` để kiểm tra trước khi đóng gói.
## V1.2.4
- Khi chủ phòng đóng tab/trình duyệt trong trạng thái đang thi đấu, hệ thống xác nhận Offline qua presence rồi tự đóng phòng.
- Chủ phòng bị tính bỏ trận, trừ 20 RP, cộng 1 trận thua và reset chuỗi thắng.
- Khách không thay đổi RP, thống kê hoặc chuỗi; được giải phóng để tạo phòng mới.
- Giữ nguyên quyền Admin hủy phòng mà không phạt thêm người chơi.


## V1.2.7 - Fix lời mời không hiển thị
- Lời mời được kiểm tra trên mọi trang đã đăng nhập, kể cả Lịch sử và Hướng dẫn.
- Tab nền vẫn kiểm tra lời mời theo chu kỳ 10 giây.
- API đọc tối đa 20 lời mời pending để không bỏ sót lời mời hợp lệ cũ hơn.
- Lỗi truy vấn API không còn bị hiểu nhầm là không có lời mời.
- Đồng bộ cache lời mời sau khi gửi.

## V1.2.9
- Sửa lỗi người nhận đang ở trang phòng một mình không thấy lời mời.
- Polling và watchdog lời mời tiếp tục chạy trên trang `/room/...`.
- Không thay đổi điều kiện backend: phòng đủ hai người hoặc đã thi đấu vẫn không nhận lời mời mới.
- Kiểm tra hồi quy toàn bộ: 166/166 test đạt.

## V1.3.0 — 06/08/2026 21:37 (GMT+7)

### Nội dung
- Thêm lõi cấu hình chung cho 6 chế độ Rank: Rank thường Random, Random 3 chọn 1, Đấu chiến thuật BO3, BO3, Cấm chọn CLB BO3, Lượt đi – lượt về.
- Chuẩn hóa điều kiện mở khóa: RP tối thiểu, số trận Rank, chênh lệch RP.
- Chuẩn hóa bảng RP Series 2–0, 2–1, hòa và bỏ cuộc; RP chỉ trả về để áp dụng một lần khi Series kết thúc.
- Thêm hàm xác định kết quả BO3 và tổng tỷ số hai lượt; không áp dụng bàn thắng sân khách.
- Thêm giao diện chọn 6 chế độ dạng lưới gọn, có khóa và lý do khóa.
- Thêm SQL nền cho Series, trận con và lịch sử cấm/chọn CLB.
- Giữ nguyên luồng đang hoạt động của Rank thường và Random 3 chọn 1.
- Bốn chế độ Series được khóa nút bắt đầu cho đến khi chạy SQL và nối hoàn chỉnh luồng trận con, tránh tạo nhầm trận Rank thường.

### File chính
- `modules/rank_modes/catalog.py`
- `modules/rank_modes/service.py`
- `modules/rank_modes/__init__.py`
- `modules/room_team_routes.py`
- `modules/room_access_routes.py`
- `templates/room_detail.html`
- `static/style.css`
- `docs/update_rank_modes_core_v1_3_0.sql`
- `test_rank_modes_core_v130.py`

## V1.3.2 - UI MASTER phòng đấu + sắp xếp SQL
- Áp dụng bố cục phòng đấu theo ảnh UI MASTER đã chốt.
- Thêm PES ARENA nhỏ gọn ở giữa thanh đầu.
- Giữ khu chủ phòng xanh, đối thủ đỏ, chế độ đang chọn tím, trạng thái hợp lệ xanh lá.
- Thêm thẻ thông tin chế độ ở giữa và 6 thẻ chế độ nhỏ phía dưới.
- Chỉ hiển thị Tổng điểm, không dùng OVR.
- Giữ nguyên API chọn chế độ `room_select_ranked_mode` và cơ chế AJAX hiện có.
- CSS mới giới hạn trong `.room-layout-v137`, không dùng selector toàn cục.
- Gom toàn bộ SQL cũ vào `docs/sql_archive/`; chỉ để `docs/PES_ARENA_UPDATE_LATEST.sql` ở ngoài.


## V1.3.3 - Sửa mở khóa chế độ + hiển thị desktop 100%
- Sửa nguồn RP mở khóa: ưu tiên `rank_points`, giữ fallback `rating`/`rp`.
- Sửa số trận Rank: ưu tiên tổng `wins + draws + losses`, tránh `total_matches` cũ khóa sai.
- Sửa kiểm tra chênh RP của đối thủ dùng đúng `rank_points`.
- Loại bỏ khối CSS UI MASTER bị lặp hai lần.
- Thêm breakpoint theo chiều cao màn hình để desktop zoom 100% nhìn được khu thi đấu và 6 chế độ.
- Không thay đổi API, polling, luồng tạo phòng/mời đấu/sẵn sàng/thoát phòng.

## V1.3.7 - 2026-08-06 23:08 (Asia/Bangkok)

### Nội dung
- Ghép bộ logo WebP do người dùng cung cấp vào UI phòng đấu V2.
- Thay logo PES ARENA ở thanh tiêu đề.
- Thay VS emblem.
- Thay icon đủ 6 chế độ Rank.
- Tách icon card và emblem lớn ở card chế độ trung tâm để đúng tỷ lệ từng logo.
- Giữ nguyên nút hành động bằng CSS vì nội dung và trạng thái nút là dữ liệu động.
- Giữ toàn bộ file WebP gốc trong `static/assets/room_v2/source_user_logo/`.

### File sửa
- `app.py`
- `templates/room_detail.html`
- `static/css/arena_room_v2.css`
- `static/assets/room_v2/pes-arena-room-logo.webp`
- `static/assets/room_v2/vs-gold-emblem.webp`
- `static/assets/room_v2/modes/*.webp`
- `static/assets/room_v2/emblems/*.webp`
- `static/assets/room_v2/USER_LOGO_MAPPING.txt`

### So với V1.3.6
- V1.3.6 dùng bộ asset minh họa tự tạo.
- V1.3.7 dùng đúng bộ logo WebP người dùng đã chuẩn bị và căn chỉnh riêng theo từng vị trí UI.


## V1.3.8 — Room UI CSS/Neon cleanup
- Fixed overlapping center action controls by using one 3-column grid.
- Consolidated logo sizing into one CSS flow.
- Standardized neon hierarchy.
- Removed unused room_master.css, legacy SVG mode icons, source logo dump, stale UI tests and caches.
- Added exact Supabase upload manifest and audit report.

## V1.3.10 — Supabase Room Asset Upload Pack

- Thêm thư mục `UPLOAD_SUPABASE/UPLOAD_VAO_BUCKET_public-assets/room-assets/v1.3.10/` chứa đúng 20 file WebP cần upload.
- Thêm manifest CSV ghi rõ bucket, object path, URL public mẫu, dung lượng và SHA-256.
- Thêm biến `ROOM_ASSET_BASE_URL` và helper `room_asset()`; khi chưa cấu hình, hệ thống tự dùng asset local.
- Không thay đổi API hoặc logic phòng đấu.

## V1.3.10 — Fix tên chế độ và nút Neon
- Đổi tên thẻ chế độ desktop: Random, 3 chọn 1, Chiến thuật BO3, BO3, Cấm chọn BO3, Lượt đi/về.
- Tách class vai trò cho Mời đấu, Tìm nhanh/Sẵn sàng và Thoát phòng.
- Sửa xung đột với rule `.btn` toàn cục có `!important` trong `static/style.css`.
- Ba nút dùng Grid 3 cột, không chồng, không chung nền.
- Không đổi route/API hoặc logic sẵn sàng, tìm nhanh, thoát phòng.

## V1.3.11 - Ghép trực tiếp Supabase pes-assets
- Chuyển gói upload sang bucket thật `pes-assets`.
- Folder đích: `room-assets/v1.3.11`.
- Ghép sẵn public URL `https://wlnvdfghatgeygecwrqb.supabase.co/storage/v1/object/public/pes-assets/room-assets/v1.3.11` vào helper asset phòng đấu.
- Không bắt buộc cấu hình biến Vercel; `ROOM_ASSET_BASE_URL` vẫn có thể dùng để ghi đè.
- Làm lại `UPLOAD_SUPABASE` và manifest chi tiết đúng bucket của dự án.


## V1.3.12 - Chuẩn hóa tỷ lệ UI MASTER phòng đấu
- Chỉnh Grid desktop theo tỷ lệ 31% / 24% / 31% / 14%, gap 12px.
- Dựng lại tỷ lệ card Host/Opponent, nền sân, light effect, avatar, rank, vùng CLB và Tổng điểm.
- Tăng tỷ lệ card chế độ trung tâm, emblem và VS; căn lại hàng 3 nút Neon.
- Tăng chiều cao 6 card chế độ, thu gọn sidebar Info/Parsec và chuẩn hóa typography/neon.
- Không đổi API, route, polling hoặc logic phòng đấu. Không có SQL mới.


## V1.3.19 - Fix state action dock
- Giữ hiển thị Sẵn sàng, Hủy sẵn sàng, Thoát phòng và các nút theo trạng thái ở đáy khu trung tâm.
- Giữ bảng nhập tỷ số và nút Gửi kết quả trong vùng nhìn thấy khi trận đang Playing.
- Không thay route, API, RP hoặc logic trạng thái phòng.

## V1.3.20 — 2026-08-07
- Sửa nút Quay quân của chế độ 3 chọn 1 bị nền/viền hồng tím do rule legacy `.room-center-random-trigger.random3-trigger` trong `static/style.css`.
- Thêm override giới hạn trong `.arena-room-v2`: bỏ toàn bộ nền tím, viền tím và glow tím của wrapper.
- Giữ riêng nút QUAY QUÂN màu vàng gold, subtitle nằm bên dưới nền trong suốt.
- Không sửa route, API, trạng thái phòng hoặc luồng random 3 CLB.
