# PES Arena V1.14.41.67

## Giới hạn trận cuối tuần
- Thứ Hai–Thứ Sáu: 10 trận Rank/ngày.
- Thứ Bảy–Chủ Nhật: 15 trận Rank/ngày.
- Múi giờ áp dụng: Việt Nam (GMT+7), reset lúc 00:00.

## Sửa tạo quá nhiều phòng
- Sửa truy vấn phòng active từ bảng sai `rooms` sang bảng đúng `match_rooms`.
- Phòng `waiting_ready` được coi là phòng active.
- Một người đang có phòng chờ sẽ được chuyển về phòng đó thay vì tạo phòng mới.
- Dọn an toàn phòng chờ trùng chưa có `match_id`.
- Không xóa phòng đang thi đấu, chờ kết quả, tranh chấp hoặc có trận liên kết.
- Tự hủy lời mời pending thuộc phòng trùng đã xóa.

## Kiểm tra
- 101/101 test đạt.
