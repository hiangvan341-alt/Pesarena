## V1.14.41.20 — 2026-07-30 18:55 (Asia/Bangkok)
- Sửa logo Parsec hiển thị chưa đầy đủ: bỏ khung vuông 18x18, dùng 20x30 theo tỷ lệ dọc.
- File: `static/css/parsec_room.css`, `templates/partials/parsec_room_panel.html`.

# V1.14.41.14 — Rà soát CSS toàn dự án

- Thời gian: 30/07/2026 18:08 (Asia/Bangkok)
- Chuẩn hóa font toàn dự án qua `--app-font`.
- Xóa 5 rule CSS trùng hoàn toàn.
- Module Parsec kế thừa font chung.
- Kiểm tra và cố định thứ tự nạp CSS.
- File sửa: `static/style.css`, `static/css/parsec_room.css`, `templates/base.html`, `app.py`.

---

# V1.14.41.13 — Chuẩn hóa giao diện module Parsec

- Làm lại riêng module Parsec theo ảnh mẫu; không thay đổi các khung phòng đấu khác.
- Khóa logo Parsec 18 × 18 px trong đúng file CSS của module.
- Xóa CSS bảo vệ logo bị lặp trong `static/style.css` và bỏ toàn bộ inline CSS trên ảnh logo.
- Nút Copy ID chuyển về nền xanh đen, viền vàng mảnh; nút Copy Link giữ màu hồng theo ảnh mẫu.
- Đồng bộ font Inter/Segoe UI/Arial trong toàn bộ module và cho button/input/select/textarea kế thừa font chung.
- Sắp xếp cột phải cố định: Thông tin phòng → Parsec → Lịch sử đấu → Chat.
- Giữ nguyên phân quyền chủ phòng/khách và toàn bộ logic lưu, xóa, sao chép Parsec.

# V1.14.41.12 — Sửa logo Parsec bị phóng to

- Nguyên nhân chính: `parsec_room.css` được gọi qua `asset_url()`, nên khi `STATIC_ASSET_BASE_URL` trỏ Supabase, trang có thể tải bản CSS cũ trên Supabase thay vì CSS mới trong dự án.
- Chuyển `parsec_room.css` về tải trực tiếp từ `/static/css/parsec_room.css`.
- Khóa logo Parsec ở 18×18 px bằng 3 lớp bảo vệ: thuộc tính HTML, inline `!important`, và quy tắc dự phòng cuối `static/style.css`.
- Ảnh logo vẫn được phép tải từ Supabase; chỉ CSS điều khiển kích thước được giữ cục bộ để tránh cache/bản cũ.

File sửa:
- `templates/base.html`
- `templates/partials/parsec_room_panel.html`
- `static/css/parsec_room.css`
- `static/style.css`
- `app.py`


## V1.14.41.8 — 2026-07-30 16:54 (Asia/Bangkok)
- Sửa lỗi khối Parsec chỉ có trong fragment polling, chưa có trong trang phòng tải lần đầu.
- Chuyển khối Parsec sang cột thông tin bên phải.
- Thu nhỏ logo Parsec còn 22×22 px, lưu `static/parsec-logo.webp`.
- Frontend gọi logo qua `asset_url()` để dùng Supabase khi `STATIC_ASSET_BASE_URL` đã cấu hình.
- Rút gọn tên phiên bản hiển thị thành `V1.14.41.8`.
- Điều chỉnh logo PES Arena dùng `object-fit: contain`, không cắt nội dung và tăng vùng hiển thị.
- Không thêm polling và không thay đổi RP.
# Collap V1.14.40 — Shop & Inventory Phase 3

- Nền phát triển duy nhất: `Collap_V1.14.39.12`.
- Thêm Cửa hàng `/shop`, Kho đồ `/inventory` và Admin Shop `/admin/shop` dưới dạng module độc lập.
- Seed 25 vật phẩm từ `Cuahang.rar`: 6 khung avatar, 6 banner, 5 huy hiệu, 3 màu tên, 1 vé đổi tên và 4 phiếu giảm giá.
- Phiếu 20% và 30% không được bày bán; chỉ Admin cấp cho một người hoặc toàn bộ người chơi.
- Mua hàng bằng RPC nguyên tử, có chống gửi trùng, lịch sử giao dịch và hỗ trợ phiếu giảm giá.
- Trang bị đồng thời 1 khung avatar, 1 banner, 1 màu tên và 1 huy hiệu cạnh tên.
- Vé đổi tên được tiêu thụ sau khi dùng hết 2 lượt miễn phí.
- Cần chạy `docs/update_shop_inventory_phase3_v1_14_40.sql`.

# Collap V1.14.39.12

- Nền phát triển: Collap_V1.14.39.11, vốn quay lại từ V1.14.39.8.
- Đổi chống lặp đội thành lịch sử theo từng cặp đối thủ.
- Mỗi người bị loại các CLB chính mình đã dùng trong đúng 5 trận confirmed gần nhất với đối thủ hiện tại.
- Khi đổi sang đối thủ khác, lịch sử của cặp cũ không còn áp dụng.
- Rank thường và Random 3 chọn 1 dùng chung một lịch sử 5 trận.
- Vẫn bảo đảm hai bên trong cùng lượt random không nhận trùng CLB.
- Chuẩn hóa tên CLB bằng strip/casefold để tránh trùng do chữ hoa hoặc khoảng trắng.
- Không cần chạy SQL.

# Collap V1.14.39.11

- Nền: Collap V1.14.39.10.
- Rank thường: mỗi người không được nhận lại CLB đã sử dụng trong đúng 5 trận Rank thường đã xác nhận gần nhất.
- Bỏ cơ chế nới lịch sử cấm xuống 1 hoặc 0 trận; bảo đảm 5 CLB gần nhất luôn bị loại.
- Random 3 chọn 1: giữ nguyên cơ chế đội đã chọn không xuất hiện ở lượt sau.
- Không thay đổi SQL hoặc cấu trúc Supabase.

# Collap V1.14.39.7

- Thay đổi Giới hạn thi đấu Rank mỗi ngày: không còn chặn tạo phòng, mời đấu, vào phòng, Sẵn sàng hoặc Đá tiếp.
- Trận thứ 11 trở đi trong ngày thường và trận thứ 16 trở đi vào cuối tuần vẫn được chơi và lưu lịch sử.
- Trận vượt giới hạn nhận 0 RP cho cả hai, không tác động chuỗi thắng/thua và không phát danh hiệu.
- Ghi rõ lý do không tính RP trong `matches.note` và `rp_details.daily_rank_limits`.
# Collap V1.14.39.10

- Quay lại hoàn toàn nền mã nguồn `Collap_V1.14.39.8`; không sử dụng các thay đổi giao diện/polling của V1.14.39.9.
- Rank thường: mỗi người không được nhận lại CLB đã dùng trong đúng 3 trận Rank thường đã xác nhận gần nhất.
- Random 3 chọn 1: CLB người chơi thực sự đã chọn trong các trận đã xác nhận sẽ không xuất hiện trong các lượt Random 3 chọn 1 tiếp theo của chính người đó.
- Các CLB chỉ xuất hiện trong 3 lựa chọn nhưng không được chọn vẫn có thể xuất hiện lại.
- Trong cùng một lượt Random 3 chọn 1, 6 lựa chọn của hai bên vẫn không trùng nhau.
- Không cần chạy SQL.

# Collap V1.14.41.2 — Security, Test & Cleanup Hotfix

- Thời gian: 30/07/2026 15:34 (Asia/Bangkok).
- Nền phát triển: `Collap_V1.14.41.1_GLOBAL_NAME_STYLE_TICKET_ONLY_HOTFIX`.
- `app.py`: đổi `APP_VERSION` thành `Collap_V1.14.41.2_SECURITY_TEST_CLEANUP_HOTFIX`.
- `app.py`: bỏ secret Flask mặc định công khai; Production/Preview sẽ dừng rõ lỗi nếu thiếu `FLASK_SECRET_KEY`. Chỉ Test/Development được tạo secret tạm thời.
- `test_rp_engine.py`: cập nhật phiên bản công thức từ `RP_V1.14.2` lên `RP_V1.14.3`, chuyển thành 7 test mà `pytest` có thể tự nhận diện, vẫn giữ cách chạy trực tiếp bằng Python.
- `.env.example`: ghi rõ `FLASK_SECRET_KEY` là bắt buộc trên Vercel và khuyến nghị chuỗi ngẫu nhiên dài.
- Xóa toàn bộ `__pycache__` và file `*.pyc` khỏi gói phát hành.
- Kiểm tra module Zcoin: `app.py` đang dùng package `modules/zcoin/`; giữ các file Zcoin cũ để tránh phá tương thích, không đăng ký route trùng.
- Không sửa và không tự chạy SQL. Vẫn cần chạy đúng `docs/update_global_name_style_ticket_only_v1_14_41_1.sql` trên Supabase tương ứng.

## V1.14.41.3 — 30/07/2026 15:40 (Asia/Bangkok)

### Sửa thống kê Random 3 chọn 1
- `modules/admin_dashboard_routes.py`: báo cáo Admin không còn chỉ phụ thuộc vào `matches.note`; ưu tiên nhận diện qua `match_rooms.team_tier` và `matches.rp_details.match_mode`.
- Khôi phục thống kê cho các trận lịch sử đã bị ghi đè ghi chú thành `Đã xác nhận.` nếu phòng đấu liên kết vẫn còn dữ liệu `random3_pick1`.
- `modules/match_result_service.py`: khi xác nhận trận, lưu `match_mode` vào `rp_details` và giữ marker `[MODE:random3_pick1]` trong ghi chú đối với Random 3 chọn 1.

### Kiểm tra
- Biên dịch toàn bộ Python: đạt.
- Pytest RP Engine: 7/7 test đạt.

### Quy tắc giới hạn Rank được đề xuất
- Trận hòa vẫn tính một lượt Rank vì trận đã bắt đầu và sử dụng giới hạn thi đấu trong ngày.
- Khi một người đã hết lượt Rank nhưng người còn lại vẫn còn lượt: nên chuyển trận thành không tính RP cho cả hai và không trừ lượt của người còn lượt. Chưa tự thay đổi logic này trong hotfix để tránh thay đổi luật thi đấu khi chưa được chốt.


## V1.14.41.4 — 30/07/2026 15:54 (Asia/Bangkok)

### Hoàn thiện giới hạn trận Rank công bằng

- `modules/daily_rank_limit_service.py`: đọc thêm `rp_details` khi đếm trận và chỉ tính lượt cho người có ID trong `daily_rank_limits.counted_user_ids`.
- Nếu một trong hai người đã hết giới hạn trước trận hiện tại, trận vẫn được lưu nhưng không cộng/trừ RP, không tính chuỗi và không chiếm lượt của cả hai. Người vẫn còn lượt vì vậy không bị mất lượt oan.
- Trận hợp lệ trong giới hạn lưu `counted_user_ids` gồm cả hai người; trận vượt giới hạn lưu danh sách rỗng và `count_rule=neither_player`.
- `modules/match_result_service.py`: ghi nhãn lịch sử rõ ràng: “Không tính RP và không tính lượt vì một trong hai người đã hết giới hạn trận Rank trong ngày.”
- `modules/admin_ranking_rebuild.py`: đồng bộ cùng quy tắc khi Admin tính lại RP, tránh rebuild làm tăng lại lượt của các trận ngoài giới hạn.
- `test_daily_rank_limit.py`: thêm 6 test cho trận hòa, trận cũ, trận hợp lệ, trận vượt giới hạn, người 11/10 đấu người 7/10 và trận thứ 10.
- Tổng kiểm thử: 13 test đạt. Không cần SQL mới.

## V1.14.41.5 — 30/07/2026 16:02 (Asia/Bangkok)

### Nội dung
- Tích hợp module công tắc riêng `Rank thường` và `Random 3 chọn 1` vào bản V1.14.41.4.
- Khi Rank thường tắt, Random 3 chọn 1 tự bật để không khóa toàn bộ chế độ Rank.
- Phòng Rank mới và phòng Rank thường đang chờ được chuyển sang Random 3 chọn 1.
- Không can thiệp trận đang chơi hoặc đang chờ xác nhận.
- Đồng bộ luồng chọn chế độ, quay đội, đá tiếp và xác nhận kết quả.
- Ẩn thẻ Rank thường và căn giữa giao diện khi chỉ còn một chế độ.
- Thêm CSS riêng `static/css/rank_mode_toggle.css`.
- Thêm 6 test cho logic và dây nối tích hợp công tắc Rank.

### File chính
- `app.py`
- `modules/admin_system_routes.py`
- `modules/room_rematch_routes.py`
- `modules/room_result_routes.py`
- `modules/room_team_routes.py`
- `modules/rank_mode_toggle/__init__.py`
- `modules/rank_mode_toggle/service.py`
- `templates/admin.html`
- `templates/room_detail.html`
- `templates/_room_live_content.html`
- `templates/partials/room_dynamic_state.html`
- `templates/base.html`
- `static/css/rank_mode_toggle.css`
- `test_rank_mode_toggle.py`
- `UPDATE_MANIFEST_V1.14.41.5.md`

## V1.14.41.6 — 2026-07-30 16:09 (Asia/Bangkok)
- Thêm module `modules/parsec_room/` tách riêng.
- Lưu `parsec_id` trong hồ sơ người chơi; chỉ thành viên cùng phòng mới được thấy ID của nhau.
- Chủ phòng được thêm, sửa hoặc xóa link Parsec tạm thời; link không bắt buộc.
- Khách chỉ được sao chép ID/link, không được sửa link.
- Backend chỉ chấp nhận HTTPS và hostname chính xác `parsec.gg`, đường dẫn dạng `/g/...`; chặn domain giả và userinfo/port/fragment bất thường.
- Dùng lại polling/state key hiện có của phòng, không tạo polling mới.
- Không sửa công thức RP, bảng matches hoặc logic giới hạn Rank.
- Thêm SQL `docs/update_parsec_room_v1_14_41_6.sql`.
- Kiểm tra: 27 test đạt; Python compile đạt; Jinja parse đạt.

## V1.14.41.7 — 2026-07-30 16:22 (Asia/Bangkok)

### Tối ưu ảnh và kiểm tra Supabase Storage
- Xóa 25 file PNG đã có file WebP cùng tên, giảm khoảng 4,68 MB trong gói triển khai.
- Giữ lại các PNG chưa có WebP tương ứng: `zalo_group_qr.png`, `rank_contact_test.png`, `rank_icons_contact_test.png`, `ranks/rank_icons_v1846_sheet.png`.
- Sửa `templates/zcoin_wallet.html` để dùng `asset_url('zcoin-logo.webp')`, không còn gọi `zcoin-logo.png` trực tiếp từ `/static`.
- Xác nhận các ảnh nền, logo, biểu tượng Rank, thẻ Rank, VS, Zcoin và ảnh Shop đều đi qua `asset_url()` ở frontend chính.
- Thêm `tools/check_supabase_assets.py` để kiểm tra toàn bộ URL trong `SUPABASE_ASSET_MANIFEST.csv` sau khi cấu hình biến môi trường thật.
- Đổi `APP_VERSION` thành `Collap_V1.14.41.7_SUPABASE_ASSET_CLEANUP`.
- Không thay đổi database, RP, polling hoặc logic phòng đấu.

## V1.14.41.9 — 2026-07-30 17:19 (Asia/Bangkok)

- Dùng đúng logo Parsec do người dùng cung cấp, tối ưu còn khoảng 1.4 KB.
- Thu nhỏ logo Parsec và đặt trong khung trắng gọn, không còn bị phóng lớn.
- Làm lại thẻ Parsec theo giao diện compact ở cột phải.
- Đồng nhất giao diện chủ phòng và khách; phân quyền sửa/xóa link vẫn giữ nguyên.
- Tách giao diện Parsec thành partial dùng chung để tránh hai template lệch nhau.
- Sắp xếp lại thứ tự cột phải: Thông tin phòng → Parsec → Lịch sử → Chat.
- Rút gọn `APP_VERSION` thành `V1.14.41.9`.

## V1.14.41.10 — 2026-07-30 17:44 (Asia/Bangkok)

- Tách nền logo Parsec từ file người dùng cung cấp, giữ đúng biểu tượng và tránh nền xám/ trắng.
- Làm lại khối `KẾT NỐI PARSEC` theo bố cục gần với ảnh mẫu: logo nhỏ bên trái, tiêu đề gọn, các hàng dữ liệu dạng ô nhập tối màu và nút đồng bộ với giao diện phòng đấu.
- Giao diện khách hiển thị `ID Parsec`, `ID của bạn` và nút `Copy Link Parsec` theo kiểu gọn.
- Giao diện chủ phòng hiển thị `ID chủ phòng`, `ID khách`, trường nhập link và nút `Lưu` / `Xóa` rõ ràng hơn.
- Đồng nhất font và cỡ chữ trong panel Parsec để bớt lệch với phần còn lại của giao diện.
- Cập nhật `APP_VERSION` thành `V1.14.41.10`.

## V1.14.41.11 — 2026-07-30 17:57 (Asia/Bangkok)

- Chỉnh lại giao diện khối `KẾT NỐI PARSEC` theo đúng bố cục mẫu: tiêu đề gọn, logo nhỏ, trường `ID Parsec`, trường `Link Parsec`, nút `Copy ID` và `Copy Link Parsec` đồng bộ với ảnh mẫu.
- Thu nhỏ logo Parsec bằng kích thước cố định trong CSS để tránh tình trạng logo hiển thị quá lớn sau khi deploy.
- Giao diện khách được tối giản gần với mẫu tham chiếu: chỉ hiển thị `ID Parsec`, `Link Parsec` và ghi chú ngắn bên dưới.
- Giao diện chủ phòng vẫn giữ quyền sửa/xóa link nhưng dùng lại cùng hệ thống font, màu và spacing để đỡ lệch giao diện.
- Cập nhật `APP_VERSION` thành `V1.14.41.11`.

## V1.14.41.17 — 2026-07-30 18:29 (Asia/Bangkok)
- Tạo lại bản đầy đủ từ V1.14.41.15.
- Giữ toàn bộ module và mã nguồn dự án.
- Áp dụng sửa CSS Parsec chống màu vàng ghi đè.
- Chỉ bỏ các ảnh đã có trên Supabase theo `SUPABASE_ASSET_MANIFEST.csv`.

## V1.14.41.18 — 2026-07-30 18:36 (Asia/Bangkok)
- Sửa định dạng Parsec ID để chấp nhận dấu `#` và dãy số phía sau.
- Ví dụ hợp lệ: `Salem6556#18473949`.
- Đồng bộ HTML pattern, backend validator và constraint Supabase.

## V1.14.41.19 — 30/07/2026 18:52 (Asia/Bangkok)
- Rà soát cuối CSS/request/polling/tài nguyên.
- Sửa `templates/base.html`; xóa 2 ảnh test không dùng; thêm báo cáo audit.

## V1.14.41.21
- Sửa logo dự án PES Arena ở sidebar hiển thị đầy đủ; bỏ giới hạn chiều cao/chiều rộng gây cắt hoặc thu thiếu.
- Hoàn tác thay đổi nhầm kích thước logo Parsec về 18×18 px.

## V1.14.41.22 — 2026-07-30 22:49 (Asia/Bangkok)

- Sửa Random 3 chọn 1 đôi khi báo không có CLB phù hợp.
- Giữ 6 lựa chọn trong cùng lượt luôn khác nhau.
- Khi Tier theo Rank hết CLB, tự chuyển sang Tier gần nhất còn phù hợp.
- Khi lịch sử đối đầu làm cạn pool, chỉ nới lịch sử; không cho trùng đội trong lượt hiện tại.
- File sửa: `app.py`, `UPDATE_MANIFEST_V1.14.41.22.md`, `Log.md`.
- Kiểm tra: 31/31 test thành công.

## V1.14.41.23 — 2026-07-31 01:29 (Asia/Bangkok)
- Sửa `/admin/system/features` bị 500 khi tắt Random 3 và bật Rank thường.
- Chuyển hậu xử lý phòng cũ sang cơ chế best-effort, không làm lỗi thao tác lưu.
- Khi tắt Random 3, phòng đang chờ chuyển về Rank thường (`Smart Tier Random`).
- Thêm xác nhận 6 lựa chọn Random 3 phải là 6 CLB khác nhau.
- File sửa: `app.py`, `modules/admin_system_routes.py`.
- File thêm: `test_random3_safety_source.py`, `UPDATE_MANIFEST_V1.14.41.23.md`.

## V1.14.41.23 — 2026-07-31 01:29 (Asia/Bangkok)
- Sửa `/admin/system/features` bị 500 khi tắt Random 3 và bật Rank thường.
- Chuyển hậu xử lý phòng cũ sang cơ chế best-effort, không làm lỗi thao tác lưu.
- Khi tắt Random 3, phòng đang chờ chuyển về Rank thường (`Smart Tier Random`).
- Thêm xác nhận 6 lựa chọn Random 3 phải là 6 CLB khác nhau.
- File sửa: `app.py`, `modules/admin_system_routes.py`.
- File thêm: `test_random3_safety_source.py`, `UPDATE_MANIFEST_V1.14.41.23.md`.

## V1.14.41.24
- Thời gian: 2026-07-31 01:34 (Asia/Bangkok)
- Sửa hiện diện Online/Offline và nút Tìm Nhanh.
- File sửa: `app.py`, `templates/base.html`.
- Thêm: `UPDATE_MANIFEST_V1.14.41.24.md`.
- Kiểm thử: 33/33.

## V1.14.41.25 — 31/07/2026 01:43 (Asia/Bangkok)

- Sửa Tìm Nhanh không phát hiện người chơi online do đọc danh sách cache.
- Truy vấn presence trực tiếp từ Supabase bằng `last_seen_at`.
- Thêm modal thông báo đồng bộ PES Arena, bỏ `window.alert()` trong luồng Tìm Nhanh.
- Kiểm tra Python compile và 33/33 test thành công.

## V1.14.41.26 — 2026-07-31 01:46 (Asia/Bangkok)
- Riêng Admin/Owner có thể tự chọn trạng thái hiển thị Online hoặc Offline.
- Thêm bộ chọn trạng thái trên thanh trên cùng.
- Heartbeat tôn trọng chế độ Offline do Admin lựa chọn, không tự bật Online lại.
- Người chơi thường không có quyền chọn thủ công.
- Không cần SQL mới.
- Kiểm thử: 33/33 thành công.
