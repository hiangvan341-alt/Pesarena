# UPDATE MANIFEST V1.14.41.7

## Mục tiêu
Dọn các PNG đã có WebP, buộc frontend dùng ảnh WebP/Supabase và bổ sung công cụ xác minh bucket Supabase.

## File thay đổi
- `app.py`
- `templates/zcoin_wallet.html`
- `tools/check_supabase_assets.py`
- `Log.md`
- `UPDATE_MANIFEST_V1.14.41.7.md`

## File đã xóa
- `static/login-background.png`
- `static/pes-arena-logo.png`
- `static/podium_top3_reference.png`
- `static/vs.png`
- `static/zcoin-logo.png`
- 20 file PNG trong `static/ranks/` đã có WebP cùng tên.

## Cấu hình Supabase bắt buộc để dùng Storage
```text
STATIC_ASSET_BASE_URL=https://PROJECT.supabase.co/storage/v1/object/public/pes-assets/v1
SHOP_ASSET_BASE_URL=https://PROJECT.supabase.co/storage/v1/object/public/pes-assets/v1/shop
```

Nếu các biến này để trống, website vẫn dùng WebP trong `/static` làm fallback.

## Kiểm tra sau triển khai
Trên Windows PowerShell:
```powershell
$env:STATIC_ASSET_BASE_URL="https://PROJECT.supabase.co/storage/v1/object/public/pes-assets/v1"
$env:SHOP_ASSET_BASE_URL="https://PROJECT.supabase.co/storage/v1/object/public/pes-assets/v1/shop"
python tools/check_supabase_assets.py
```

Kết quả phải báo toàn bộ tài nguyên `OK` trước khi xóa fallback WebP khỏi Vercel.

## SQL
Không có SQL mới.
