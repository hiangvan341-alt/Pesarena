# PES Arena V1.3.39 — Mode Logos

## Mapping

| File nguồn | Chế độ | Asset web |
|---|---|---|
| 1.webp | Đấu chiến thuật BO3 | tactical_bo3.webp |
| 2.webp | Cấm chọn CLB BO3 | ban_pick_bo3.webp |
| 3.webp | Rank thường Random | rank_random.webp |
| 4.webp | Random 3 chọn 1 | random3_pick1.webp |
| 5.webp | Lượt đi – lượt về | home_away.webp |
| 6.webp | BO3 | bo3.webp |

## Hiển thị

Logo được đặt trong viewport cố định và dùng `object-fit: contain`; kích thước pixel hay tỉ lệ ảnh nguồn không quyết định kích thước hiển thị.

## Supabase

Bucket `pes-assets`, đè đúng 12 file trong `room-assets/v1.3.18/modes/` và `room-assets/v1.3.18/emblems/`. Template gắn query `?v=1.3.39` để phá cache.
