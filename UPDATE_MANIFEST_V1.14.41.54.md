# UPDATE MANIFEST — V1.14.41.54

## Mục tiêu
Chỉ giữ chức năng **Hủy phòng** trong Admin. Hủy phòng nhằm giải phóng trạng thái để người chơi có thể tạo phòng mới và tuyệt đối không làm thay đổi RP.

## Thay đổi
- Bỏ endpoint và nút **Xóa phòng** khỏi Admin.
- Hủy được mọi phòng: phòng mới có một người, chưa có trận, đang chơi, đã nhập kết quả, chờ xác nhận, đang tranh chấp, có báo cáo hoặc đã hoàn tất.
- Không gọi hoàn tác RP khi Admin hủy phòng.
- Trận đã `confirmed` được giữ nguyên trạng thái, tỷ số và `delta1/delta2`.
- Trận đang `playing`, `waiting_confirm` hoặc `disputed` chuyển sang `cancelled` chỉ để giải phóng khóa trận; không sửa tỷ số, delta, báo cáo hay bằng chứng tranh chấp.
- Bản ghi phòng chuyển sang `cancelled`; lời mời liên kết được hủy.
- Giữ nguyên lịch sử, báo cáo và dữ liệu tranh chấp.

## File thay đổi
- `app.py`
- `modules/admin_data_routes.py`
- `templates/admin.html`
- `Log.md`
