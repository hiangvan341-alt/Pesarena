# Lucky Box Giai đoạn 2B · V1.14.41.43

## Phạm vi

- Trang quản trị Lucky Box tại `/admin/lucky-box`.
- Chỉnh cấu hình hộp, giá mở, phân phối 0/1/2/3 vật phẩm và chính sách vật phẩm trùng.
- Chỉnh riêng từng reward: bật/tắt, trọng số, lịch xuất hiện, giới hạn phát hành và Zcoin bồi hoàn.
- Nhân bản Rate Version thành Draft mới.
- Đồng bộ vật phẩm Shop mới vào Draft ở trạng thái tắt và trọng số 0.
- Kiểm tra cấu hình bằng cùng validator phía server dùng khi publish.
- Publish Draft thành Active, tự lưu Active cũ thành Archived.
- Nhật ký Admin lưu lý do và dữ liệu trước/sau.
- Admin Preview tiếp tục không trừ Zcoin và không phát vật phẩm.

## An toàn vận hành

- Chỉ Draft được chỉnh sửa.
- Publish không tự bật Lucky Box.
- Bật hộp bị chặn nếu chưa có Active hợp lệ.
- Migration không xóa hoặc ghi đè lịch sử.
- “Chúc bạn may mắn lần sau” vẫn bị chặn nếu chưa bật quyền ở cấu hình hộp.

## Trình tự Preview

1. Chạy `docs/update_luckybox_admin_v1_14_41_43.sql`.
2. Deploy branch Preview.
3. Đăng nhập Admin → `/admin/lucky-box`.
4. Chỉnh Draft và quay thử 1.000/10.000 lượt.
5. Chỉ publish sau khi validator báo HỢP LỆ.
6. Chưa bật hộp cho người chơi cho đến khi hoàn tất Giai đoạn 3.
