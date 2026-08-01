# Tối ưu ảnh — V1.14.41.50

## Kết quả

- Đã xóa **85** file ảnh local, giảm **8.81 MB** trong mã nguồn.
- Các ảnh nằm trong `SUPABASE_ASSET_MANIFEST.csv` đã được lược khỏi `static/`.
- Các bản PNG cũ/trùng với WebP và ảnh kiểm thử không được frontend sử dụng đã được xóa.
- QR Zalo vẫn dùng định dạng PNG trên Supabase để bảo đảm khả năng quét.
- Ba icon cúp SVG được giữ lại vì rất nhẹ, sắc nét và không cần đổi sang WebP.
- CSS đăng nhập đã đổi sang biến `--pes-login-background`, không còn gọi cứng file local đã xóa.

## Điều kiện triển khai bắt buộc

- Vercel phải có `STATIC_ASSET_BASE_URL` trỏ đúng thư mục public chứa các file trong manifest.
- Nếu dùng ảnh Shop riêng, giữ `SHOP_ASSET_BASE_URL` đúng với thư mục public tương ứng.
- Nếu dùng Lucky Box riêng, giữ `LUCKYBOX_ASSET_BASE_URL` đúng với thư mục public tương ứng.

## File đã xóa

| File | Dung lượng | Lý do |
|---|---:|---|
| `static/login-background.webp` | 202,838 bytes | Supabase manifest |
| `static/pes-arena-logo.webp` | 68,268 bytes | Supabase manifest |
| `static/podium_top3_reference.webp` | 84,084 bytes | Supabase manifest |
| `static/ranks/ban-chuyen-card.webp` | 16,808 bytes | Supabase manifest |
| `static/ranks/ban-chuyen.webp` | 12,480 bytes | Supabase manifest |
| `static/ranks/bao-thu-card.webp` | 15,480 bytes | Supabase manifest |
| `static/ranks/bao-thu.webp` | 11,070 bytes | Supabase manifest |
| `static/ranks/chuyen-nghiep-card.webp` | 17,348 bytes | Supabase manifest |
| `static/ranks/chuyen-nghiep.webp` | 12,372 bytes | Supabase manifest |
| `static/ranks/dang-cap-card.webp` | 17,860 bytes | Supabase manifest |
| `static/ranks/dang-cap.webp` | 12,426 bytes | Supabase manifest |
| `static/ranks/ga-card.webp` | 12,652 bytes | Supabase manifest |
| `static/ranks/ga.webp` | 10,008 bytes | Supabase manifest |
| `static/ranks/goat-card.webp` | 21,190 bytes | Supabase manifest |
| `static/ranks/goat.webp` | 13,486 bytes | Supabase manifest |
| `static/ranks/huyen-thoai-card.webp` | 19,240 bytes | Supabase manifest |
| `static/ranks/huyen-thoai.webp` | 12,728 bytes | Supabase manifest |
| `static/ranks/moi-tap-choi-card.webp` | 15,864 bytes | Supabase manifest |
| `static/ranks/moi-tap-choi.webp` | 11,744 bytes | Supabase manifest |
| `static/ranks/non-card.webp` | 15,058 bytes | Supabase manifest |
| `static/ranks/non.webp` | 10,904 bytes | Supabase manifest |
| `static/ranks/sieu-sao-card.webp` | 17,946 bytes | Supabase manifest |
| `static/ranks/sieu-sao.webp` | 11,898 bytes | Supabase manifest |
| `static/vs.webp` | 16,514 bytes | Supabase manifest |
| `static/zalo_group_qr.png` | 373,800 bytes | Supabase manifest |
| `static/zcoin-logo.webp` | 283,044 bytes | Supabase manifest |
| `static/shop/items/avatar_frame_common.webp` | 59,516 bytes | Supabase manifest |
| `static/shop/items/avatar_frame_epic.webp` | 93,768 bytes | Supabase manifest |
| `static/shop/items/avatar_frame_fire_warrior.webp` | 87,120 bytes | Supabase manifest |
| `static/shop/items/avatar_frame_ice_elite.webp` | 73,222 bytes | Supabase manifest |
| `static/shop/items/avatar_frame_legendary_crown.webp` | 81,194 bytes | Supabase manifest |
| `static/shop/items/avatar_frame_rare.webp` | 67,492 bytes | Supabase manifest |
| `static/shop/items/discount_coupon_05.webp` | 27,660 bytes | Supabase manifest |
| `static/shop/items/discount_coupon_10.webp` | 48,096 bytes | Supabase manifest |
| `static/shop/items/discount_coupon_20.webp` | 50,032 bytes | Supabase manifest |
| `static/shop/items/discount_coupon_30.webp` | 45,044 bytes | Supabase manifest |
| `static/shop/items/display_name_change_ticket.webp` | 51,730 bytes | Supabase manifest |
| `static/shop/items/name_style_champion_gold.webp` | 36,870 bytes | Supabase manifest |
| `static/shop/items/name_style_elite_purple.webp` | 44,894 bytes | Supabase manifest |
| `static/shop/items/name_style_neon_blue.webp` | 40,202 bytes | Supabase manifest |
| `static/shop/items/profile_badge_elite_crown.webp` | 45,420 bytes | Supabase manifest |
| `static/shop/items/profile_badge_elite_crown_96.webp` | 3,616 bytes | Supabase manifest |
| `static/shop/items/profile_badge_fire_streak.webp` | 54,504 bytes | Supabase manifest |
| `static/shop/items/profile_badge_fire_streak_96.webp` | 4,084 bytes | Supabase manifest |
| `static/shop/items/profile_badge_legendary_diamond.webp` | 55,270 bytes | Supabase manifest |
| `static/shop/items/profile_badge_legendary_diamond_96.webp` | 4,110 bytes | Supabase manifest |
| `static/shop/items/profile_badge_pitch_warrior.webp` | 31,902 bytes | Supabase manifest |
| `static/shop/items/profile_badge_pitch_warrior_96.webp` | 2,812 bytes | Supabase manifest |
| `static/shop/items/profile_badge_rising_rookie.webp` | 41,296 bytes | Supabase manifest |
| `static/shop/items/profile_badge_rising_rookie_96.webp` | 3,606 bytes | Supabase manifest |
| `static/shop/items/profile_banner_fire.webp` | 91,658 bytes | Supabase manifest |
| `static/shop/items/profile_banner_ice.webp` | 107,806 bytes | Supabase manifest |
| `static/shop/items/profile_banner_legendary_red_purple.webp` | 97,954 bytes | Supabase manifest |
| `static/shop/items/profile_banner_neon_green.webp` | 72,804 bytes | Supabase manifest |
| `static/shop/items/profile_banner_stadium_blue.webp` | 45,730 bytes | Supabase manifest |
| `static/shop/items/profile_banner_stadium_premium.webp` | 97,046 bytes | Supabase manifest |
| `static/parsec-logo.webp` | 6,062 bytes | Supabase manifest |
| `static/login-background.png` | 2,437,140 bytes | legacy/test PNG |
| `static/pes-arena-logo.png` | 424,811 bytes | legacy/test PNG |
| `static/podium_top3_reference.png` | 101,404 bytes | legacy/test PNG |
| `static/rank_contact_test.png` | 1,002,438 bytes | legacy/test PNG |
| `static/rank_icons_contact_test.png` | 528,932 bytes | legacy/test PNG |
| `static/ranks/ban-chuyen-card.png` | 121,363 bytes | legacy/test PNG |
| `static/ranks/ban-chuyen.png` | 16,433 bytes | legacy/test PNG |
| `static/ranks/bao-thu-card.png` | 105,309 bytes | legacy/test PNG |
| `static/ranks/bao-thu.png` | 15,026 bytes | legacy/test PNG |
| `static/ranks/chuyen-nghiep-card.png` | 121,235 bytes | legacy/test PNG |
| `static/ranks/chuyen-nghiep.png` | 16,233 bytes | legacy/test PNG |
| `static/ranks/dang-cap-card.png` | 115,886 bytes | legacy/test PNG |
| `static/ranks/dang-cap.png` | 15,557 bytes | legacy/test PNG |
| `static/ranks/ga-card.png` | 108,905 bytes | legacy/test PNG |
| `static/ranks/ga.png` | 15,193 bytes | legacy/test PNG |
| `static/ranks/goat-card.png` | 127,990 bytes | legacy/test PNG |
| `static/ranks/goat.png` | 17,090 bytes | legacy/test PNG |
| `static/ranks/huyen-thoai-card.png` | 116,477 bytes | legacy/test PNG |
| `static/ranks/huyen-thoai.png` | 16,241 bytes | legacy/test PNG |
| `static/ranks/moi-tap-choi-card.png` | 112,515 bytes | legacy/test PNG |
| `static/ranks/moi-tap-choi.png` | 15,737 bytes | legacy/test PNG |
| `static/ranks/non-card.png` | 101,138 bytes | legacy/test PNG |
| `static/ranks/non.png` | 14,501 bytes | legacy/test PNG |
| `static/ranks/rank_icons_v1846_sheet.png` | 140,290 bytes | legacy/test PNG |
| `static/ranks/sieu-sao-card.png` | 111,129 bytes | legacy/test PNG |
| `static/ranks/sieu-sao.png` | 15,371 bytes | legacy/test PNG |
| `static/vs.png` | 16,006 bytes | legacy/test PNG |
| `static/zcoin-logo.png` | 402,687 bytes | legacy/test PNG |
