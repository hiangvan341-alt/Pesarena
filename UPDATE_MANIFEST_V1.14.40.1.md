# Collap V1.14.40.1 — Shop Asset Hotfix

Baseline: `Collap_V1.14.40_SHOP_INVENTORY_PHASE3`

## Lỗi đã sửa

- Ảnh vật phẩm Shop không hiển thị trên Vercel Preview khi `STATIC_ASSET_BASE_URL` đang trỏ tới Supabase Storage.
- Modal Xem trước không tải được khung avatar, banner, huy hiệu và ảnh tiện ích.
- Nguyên nhân: đường dẫn `shop/items/...` bị ghép sang Supabase dù các ảnh Shop đang được đóng gói trong `static/shop/items`.

## Thay đổi

- `modules/static_asset_service.py`: luôn phục vụ prefix `shop/` từ Flask static (`/static/shop/...`).
- `app.py`: tăng phiên bản lên `Collap_V1.14.40.1_SHOP_ASSET_HOTFIX`.

## Không thay đổi

- Không cần chạy lại SQL.
- Không thay đổi catalog, giá, số dư, giao dịch hoặc dữ liệu Kho đồ.
