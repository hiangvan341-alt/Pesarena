# PES Arena V1.3.48 — Bộ điều phối trận con Rank Series

## Module

- `modules/rank_series/service.py`: state machine dùng chung, tạo/chốt trận con, chốt RP Series đúng một lần.
- `modules/rank_series/repository.py`: chỉ phụ trách Supabase `match_series*`.
- `modules/rank_series/routes.py`: route bắt đầu trận tiếp theo, chọn CLB và cấm/chọn.
- `modules/rank_series/modes/home_away.py`: đúng 2 lượt, giữ hai CLB xuyên suốt, xét tổng tỷ số.
- `modules/rank_series/modes/bo3.py`: tối đa 3 trận, thắng 2 trận trước kết thúc; random CLB mới từng trận.
- `modules/rank_series/modes/tactical_bo3.py`: mỗi trận tạo 3 CLB riêng cho mỗi người, không dùng lại CLB đã xuất hiện trong Series.
- `modules/rank_series/modes/ban_pick_bo3.py`: pool chung 20 CLB, hai bên cấm luân phiên 3 CLB/người, sau đó chọn CLB cho từng trận BO3; CLB đã thi đấu không dùng lại.
- `static/css/room/09-series-orchestrator.css`: chỉ quản lý UI Series, không absolute-position các nút hành động.

## Luồng chuẩn

`Admin rank_mode_configs_v1` → `room.team_tier` → `rank_series` → `match_series` → `match_series_games` → `matches` → xác nhận trận con → cập nhật Series → nếu chưa xong tạo trận kế → nếu xong chốt RP một lần.

Trận con luôn lưu `matches.delta1=0` và `matches.delta2=0`; W/H/B và bàn thắng vẫn được ghi để mỗi trận con tính là một trận Rank/ngày. RP chỉ được cộng/trừ ở `match_series` khi Series hoàn tất.

## Bỏ cuộc

Bỏ cuộc/thời gian chờ/host offline đóng luôn Series đang hoạt động, đánh dấu `result_code=forfeit`, đồng bộ `forfeit_user_id`, `winner_user_id`, `rp_player1/rp_player2`. Không để Series mồ côi.

## Trước khi deploy

Chạy `SUPABASE_UPDATE_V1.3.48.sql` một lần trên Supabase SQL Editor. Script idempotent.
