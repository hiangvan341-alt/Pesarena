# Cửa hàng & Kho đồ — Giai đoạn 3

## Baseline và nhánh

- Baseline: `Collap_V1.14.39.12`
- Nhánh: `feature/shop-inventory-phase3-v1.14.40`
- Phiên bản: `Collap_V1.14.40_SHOP_INVENTORY_PHASE3`

## Phạm vi đã triển khai

- Cửa hàng người chơi tại `/shop`.
- Kho đồ tại `/inventory`.
- Quản trị Shop tại `/admin/shop`.
- 25 vật phẩm từ bộ ảnh `Cuahang.rar`.
- Trang bị đồng thời 1 Khung Avatar, 1 Banner, 1 Màu Tên và 1 Huy hiệu cạnh tên.
- Xem trước vật phẩm trực tiếp trên mô phỏng Hồ sơ.
- Mua vật phẩm bằng RPC nguyên tử, có lịch sử giao dịch và chống gửi trùng.
- Phiếu giảm giá được tiêu thụ trong cùng giao dịch mua.
- Vé đổi tên được tự động tiêu thụ khi người chơi đã hết 2 lượt miễn phí.
- Admin có thể tặng vật phẩm cho một người hoặc toàn bộ người chơi.

## Quy tắc Phiếu giảm giá

- Phiếu 5% và 10% được bày bán.
- Phiếu 20% và 30% tồn tại trong catalog nhưng không được bày bán.
- Phiếu 20% và 30% chỉ được Admin cấp tại `/admin/shop`.
- Không thể dùng phiếu để mua một phiếu khác.
- Mỗi giao dịch chỉ dùng tối đa một phiếu.
- Phiếu chỉ bị trừ khi giao dịch thành công.

## Thứ tự triển khai Production

1. Sao lưu database Supabase.
2. Deploy source phiên bản mới.
3. Chạy `docs/update_shop_inventory_phase3_v1_14_40.sql` trong Supabase SQL Editor.
4. Chờ PostgREST reload schema hoặc tải lại project Supabase.
5. Mở `/admin/shop`, xác nhận đủ 25 vật phẩm.
6. Dùng tài khoản test mua một vật phẩm giá thấp.
7. Kiểm tra Zcoin, Kho đồ, trang bị và Hồ sơ.
8. Chỉ sau khi test PASS mới bật cho toàn bộ người chơi.

## Kiểm thử bắt buộc

- Không đủ Zcoin: không trừ tiền, không cấp vật phẩm.
- Gửi lặp cùng request key: chỉ phát sinh một giao dịch.
- Mua vật phẩm vĩnh viễn đã sở hữu: bị chặn.
- Mua vật phẩm tiêu hao: tăng số lượng.
- Dùng phiếu: tính đúng phần trăm, mức tối đa và giá tối thiểu.
- Trang bị món mới cùng loại: tự thay món cũ.
- Gỡ trang bị: Hồ sơ quay về giao diện mặc định.
- Phiếu 20% và 30% không xuất hiện trong Shop người chơi.
- Admin tặng phiếu 20%/30%: xuất hiện đúng trong Kho đồ.
- Đổi tên khi hết lượt miễn phí: tự trừ đúng một Vé đổi tên.

## Tài nguyên ảnh

- 6 Banner: `1600×400 WebP`.
- 19 vật phẩm vuông: `512×512 WebP`.
- 5 Huy hiệu có thêm bản `96×96 WebP` để hiển thị cạnh tên.
- Tổng tài nguyên Shop đã tối ưu còn khoảng 1,6 MB.
