# UPDATE MANIFEST V1.14.41.52

## Mục tiêu
- Xóa tài khoản nhưng giữ nguyên lịch sử đấu và RP.
- Kiểm tra, gia cố chức năng chủ phòng đưa khách ra khỏi phòng.

## File thay đổi
- `modules/data_cleanup_service.py`
- `modules/room_access_routes.py`
- `templates/admin.html`
- `app.py`
- `Log.md`

## Hành vi mới
1. “Xóa mềm” giữ nguyên bản ghi người chơi để các trận cũ vẫn tra được người tham gia.
2. Không xóa hoặc hoàn tác bất kỳ trận đã có `match_id`.
3. Tài khoản bị vô hiệu hóa đăng nhập và không còn Online/ghép trận.
4. Phòng chờ chưa bắt đầu được giải phóng an toàn.
5. Chủ phòng chỉ kích được khách khi phòng `waiting_ready` và chưa có `match_id`.
6. Kích khách không thay đổi RP; lời mời liên kết được chuyển sang `cancelled`.
