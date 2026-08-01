# Lucky Box Phase 3 · V1.14.41.44

## Phạm vi
- Trang Lucky Box trong Cửa hàng cho người chơi.
- Hiển thị giá, số dư, tỷ lệ 0–3 vật phẩm, pool reward và lịch sử.
- Mở hộp thật qua RPC nguyên tử đã có ở Phase 2A.
- Admin Preview giao diện người chơi không trừ Zcoin, không phát vật phẩm.
- Trang lịch sử và chi tiết ba phần thưởng.
- Chưa có animation; hiệu ứng mở hộp thuộc Phase 4.

## An toàn Preview
- Lucky Box vẫn phụ thuộc cờ `lucky_boxes.is_enabled`.
- Khi hộp đang tắt, người chơi không thể mở thật.
- Admin dùng `/lucky-box?preview=1&rate_version_id=...` để thử UI.
- Endpoint Admin Preview chỉ gọi RPC mô phỏng, không gọi `open_lucky_box`.

## Database
Không có migration mới. Phase 3 tái sử dụng toàn bộ bảng/RPC của Phase 2A và 2B.
