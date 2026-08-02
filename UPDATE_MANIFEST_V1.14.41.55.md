# PES Arena V1.14.41.55

## Thay đổi
- Tranh chấp chỉ áp dụng cho kết quả của trận đấu, không đổi phòng sang trạng thái `disputed`.
- Khi khách gửi tranh chấp:
  - Trận cũ chuyển sang `disputed` và chưa tính RP.
  - Phòng trở về `waiting_ready`.
  - Xóa liên kết `match_id` của trận cũ khỏi phòng.
  - Xóa tỷ số/đội của lượt cũ khỏi phòng nhưng giữ đầy đủ trong bảng trận và tranh chấp.
  - Giữ nguyên chế độ thi đấu của phòng.
- Hai người có thể tiếp tục Sẵn sàng và đá trận mới trong cùng phòng.

## File sửa
- `modules/room_result_routes.py`
- `app.py`
- `Log.md`

## Kiểm tra
- Python compile: đạt.
- Kiểm tra nguồn tranh chấp/phòng: 6/6 đạt.
