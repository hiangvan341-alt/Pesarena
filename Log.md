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
