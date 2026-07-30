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
