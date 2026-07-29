# UPDATE MANIFEST — Collap V1.14.40 Shop & Inventory Phase 3

## Nguồn gốc

- Baseline archive: `Collap_V1.14.39.12.zip`
- Baseline SHA-256: `3dbab1b18efe4e42f17fb9a08aa4a16349d63ef345923b5d7f8b33dfff4a3284`
- Asset archive: `Cuahang.rar`
- Asset SHA-256: `740c7c2593d07a2108c92046c3991bb4f3790636890f9919090f5de20bc5de09`
- Branch: `feature/shop-inventory-phase3-v1.14.40`

## Module mới

- `modules/shop/`
- `modules/inventory/`
- `modules/admin_shop/`

## Route mới

- `GET /shop`
- `POST /shop/purchase/<item_code>`
- `GET /inventory`
- `POST /inventory/equip/<inventory_id>`
- `POST /inventory/unequip/<slot>`
- `GET /admin/shop`
- `POST /admin/shop/items/<item_id>/update`
- `POST /admin/shop/grant`

## Database

Chạy duy nhất file:

`docs/update_shop_inventory_phase3_v1_14_40.sql`

File tạo hoặc bổ sung:

- `shop_items`
- `user_inventory`
- `user_equipment`
- `shop_purchases`
- `purchase_shop_item(...)`
- `equip_shop_item(...)`
- `unequip_shop_slot(...)`
- `change_display_name_with_shop_entitlement(...)`
- `admin_grant_shop_item(...)`

## Quyết định cố định

`discount_coupon_20` và `discount_coupon_30` có trong catalog nhưng bị khóa `is_listed=false`. Hai vật phẩm này chỉ được cấp từ Admin Shop.

## Kiểm tra đã chạy trong môi trường build

- Python compile: PASS.
- Jinja parse: 40/40 PASS.
- Static route scan: 129 route, 0 URL+method trùng.
- Catalog: 25 mã duy nhất, khớp 25 tài nguyên chính.
- Không đóng gói `__pycache__` hoặc `.pyc`.

## Giới hạn kiểm thử

Môi trường build không có Flask và Supabase runtime nên chưa thể chạy request tích hợp với database thật. Cần chạy checklist Production/Test Mode sau khi áp dụng SQL.
