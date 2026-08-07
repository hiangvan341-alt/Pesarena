# PES Arena V1.3.40 — Dedicated Mode Asset Path

6 logo chế độ Rank được tách sang một base URL riêng:
`pes-assets/room-assets/v1.3.40/modes/`

Mapping:
- tactical_bo3 -> 1.webp
- ban_pick_bo3 -> 2.webp
- rank_random -> 3.webp
- random3_pick1 -> 4.webp
- home_away -> 5.webp
- bo3 -> 6.webp

Các asset phòng khác tiếp tục dùng `room-assets/v1.3.18`, nên không cần upload lại.
Cả logo trên thẻ chọn chế độ và logo chế độ đang chọn đều dùng cùng `mode_asset()` để tránh phải duy trì hai bản `modes/` + `emblems/`.
