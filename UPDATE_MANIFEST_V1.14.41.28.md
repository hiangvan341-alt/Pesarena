# UPDATE MANIFEST V1.14.41.28

Thời gian: 2026-07-31 02:12 (Asia/Bangkok)

## Nội dung
- Nâng cấp Tìm Nhanh thành một lượt tìm liên tục.
- Khi đối thủ từ chối hoặc lời mời hết hạn, hệ thống tự gửi tới người phù hợp tiếp theo.
- Người vừa từ chối/không phản hồi chỉ bị bỏ qua trong lượt tìm hiện tại; không có cooldown dài hạn.
- Người đó vẫn có thể gửi/nhận lời mời thủ công và tham gia phòng ngay sau đó.
- Thông báo thành công chỉ còn: `Đã gửi lời mời đến <Tên người chơi>`.
- Lời mời Tìm Nhanh được đánh dấu riêng để không áp dụng cooldown 3 phút khi từ chối.
- Thêm API kiểm tra trạng thái lời mời Tìm Nhanh và lưu trạng thái lượt tìm trong sessionStorage.

## File sửa
- `app.py`
- `templates/base.html`
- `Log.md`

## Kiểm tra
- Python compile: thành công.
- Pytest: 33/33 bài test thành công.
