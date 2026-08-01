# V1.14.41.49 · Public Equipped Badge + Host Kick Guest

## Thay đổi

- Hiển thị huy hiệu hồ sơ đang trang bị bên cạnh tên người chơi tại **Cộng đồng Player**.
- Hiển thị huy hiệu đang trang bị của cả chủ phòng và khách trong **Phòng đấu**.
- Thêm nút **Đưa đối thủ ra khỏi phòng** cho chủ phòng.
- Chỉ cho phép kick khi phòng còn ở trạng thái `waiting_ready` và khách chưa bấm **Sẵn sàng**.
- Kick không trừ RP, dọn dữ liệu đội đã chọn và gửi thông báo cho người bị đưa ra.

## An toàn

- Không thay đổi tỷ lệ hoặc logic Lucky Box.
- Không thay đổi dữ liệu Zcoin.
- Không cần SQL migration.
- Không cho kick sau khi khách đã Sẵn sàng hoặc trận đã bắt đầu.

## Rollback

Hoàn tác commit V1.14.41.49 để trở về V1.14.41.48.
