# PES Arena V1.14.41.49

## Huy hiệu trang bị

Huy hiệu `profile_badge` đang sử dụng trong Kho đồ được hiển thị tại:

- Cộng đồng Player.
- Tên chủ phòng trong Phòng đấu.
- Tên khách trong Phòng đấu.

Dữ liệu được đọc theo lô từ `user_equipment` và `shop_items`, dùng chung cache mỹ phẩm hồ sơ để tránh truy vấn theo từng người chơi.

## Chủ phòng đưa khách ra khỏi phòng

Endpoint mới:

`POST /room/<room_id>/kick-guest`

Điều kiện:

- Người thao tác phải là chủ phòng.
- Phòng phải ở trạng thái `waiting_ready`.
- Phòng phải có khách.
- Khách chưa bấm Sẵn sàng.

Kết quả:

- Khách được đưa ra khỏi phòng.
- Không trừ RP.
- Xóa lựa chọn đội và trạng thái liên quan của lượt chờ hiện tại.
- Gửi thông báo hệ thống cho khách.
- Chủ phòng có thể mời đối thủ khác.

## Database

Không cần chạy SQL mới.
