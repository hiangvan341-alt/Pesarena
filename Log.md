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
