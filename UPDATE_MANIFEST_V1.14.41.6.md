# UPDATE MANIFEST V1.14.41.6

## Mục tiêu
Thêm Parsec ID trong hồ sơ và link Parsec tạm thời theo phòng đấu.

## Bắt buộc trước khi deploy
Chạy SQL:

`docs/update_parsec_room_v1_14_41_6.sql`

SQL thêm:
- `users.parsec_id`
- `match_rooms.parsec_link`
- Check constraint chống định dạng ID/link sai ở tầng database.

## Quyền truy cập
- Thành viên phòng: xem Parsec ID của hai người và link phòng.
- Chủ phòng: thêm/sửa/xóa link.
- Khách: chỉ sao chép.
- Người ngoài: route phòng từ chối nên không nhận dữ liệu Parsec.
- Admin không được xem dữ liệu Parsec nếu không phải thành viên phòng.

## Không ảnh hưởng
- Không thêm polling.
- Không sửa RP.
- Không sửa giới hạn Rank.
- Không lưu link vào lịch sử trận.
