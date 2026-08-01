# UPDATE MANIFEST V1.14.41.53

## Thời gian
02/08/2026 01:47 (Asia/Bangkok)

## Nội dung
- Xác nhận chủ phòng được đưa khách ra khỏi phòng kể cả khi khách đã Sẵn sàng, miễn phòng còn `waiting_ready` và chưa có `match_id`.
- Sửa Admin Hủy phòng: hoàn tác RP trước khi đổi trạng thái, giữ nguyên bản ghi phòng/trận và hủy lời mời liên kết.
- Trận chưa confirmed được hủy mà không tác động RP; trận confirmed hoàn tác RP đúng một lần rồi lưu trạng thái cancelled.
- Chặn xóa vật lý phòng đã có trận; yêu cầu dùng Hủy để giữ lịch sử.
- Chỉ cho phép xóa vật lý phòng chờ chưa phát sinh trận hoặc RP.
- Làm mới cache phòng, trận và lời mời sau thao tác Admin.

## File thay đổi
- app.py
- modules/admin_data_routes.py
- templates/admin.html
- Log.md
