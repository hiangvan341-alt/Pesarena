# Lucky Box Giai đoạn 2A · V1.14.41.42

## Trạng thái sau migration

- Lucky Box: `is_enabled=false`.
- Rate Version 1: `draft`.
- Giá mở: `0`.
- Xử lý vật phẩm trùng: `pending`.
- Ảnh “Chúc bạn may mắn lần sau”: reward đã seed nhưng `is_enabled=false`, `weight=0`.
- Không có cấu hình Production/Active.

## Admin Preview

Mở `/admin/lucky-box/preview` bằng tài khoản Admin. Có thể mô phỏng từ 1 đến 10.000 lượt. Preview dùng đúng hàm chọn reward phía PostgreSQL nhưng không trừ Zcoin, không phát vật phẩm, không tăng `issued_count` và không tạo lịch sử thật.

## Publish/Promote

RPC `publish_lucky_box_rate_version` đã có cho Giai đoạn 2B. RPC từ chối publish khi:

- giá bằng 0;
- duplicate policy còn `pending`;
- pool thiếu reward;
- weight lỗi;
- item không tồn tại/không hoạt động;
- chọn `convert_zcoin` nhưng chưa cấu hình mức bồi hoàn.

Publish không tự bật Lucky Box. Admin vẫn phải duyệt Preview và bật hộp ở bước riêng.

## Vật phẩm trùng

Khuyến nghị kiến trúc: **quy đổi Zcoin theo từng reward**, vì giữ nguyên xác suất công bố và không âm thầm quay lại món khác. Bản 2A chưa khóa quyết định này.

## Biến môi trường

`LUCKYBOX_ASSET_BASE_URL=https://wlnvdfghatgeygecwrqb.supabase.co/storage/v1/object/public/pes-assets/v1.14.41/luckybox`

## SQL cần chạy

`docs/update_luckybox_core_v1_14_41_42.sql`
