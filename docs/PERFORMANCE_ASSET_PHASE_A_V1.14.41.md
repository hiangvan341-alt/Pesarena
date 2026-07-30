# PES Arena V1.14.41 — Performance & Asset Phase A

## Phạm vi

- Hỗ trợ `SHOP_ASSET_BASE_URL` để chuyển riêng ảnh Shop lên Supabase Storage.
- Giữ fallback local khi biến môi trường chưa được cấu hình.
- Cache RAM ngắn cho System Features, Quick Match, hệ số gặp lại và chuông thông báo.
- Gate RAM cho batch giảm RP, tránh đọc `system_settings` ở mọi request.
- Giảm tần suất polling phụ; giữ polling trạng thái phòng theo cơ chế thích ứng hiện tại.
- Không hiển thị chat nổi trên trang Chat đầy đủ, tránh hai poller cùng tải một nội dung.

## Quy trình chuyển ảnh an toàn

1. Chạy `python tools/build_supabase_asset_bundle.py`.
2. Upload nội dung thư mục `build/supabase-assets/v1.14.41` vào bucket public `pes-assets`.
3. URL đích phải có dạng `.../pes-assets/v1.14.41/shop/...`.
4. Chạy `python tools/verify_remote_assets.py <URL_KET_THUC_BANG_v1.14.41/shop>`.
5. Chỉ khi PASS mới thêm `SHOP_ASSET_BASE_URL` vào Vercel Preview.
6. Test Shop, Kho đồ, Hồ sơ, Players và Phòng đấu trước khi áp dụng Production.

## Lưu ý

Bản Phase A chưa xóa ảnh local. Điều này cố ý để rollback nhanh. Sau khi Storage ổn định, Phase B mới loại file local nặng và PNG legacy khỏi deployment.
