# PES Arena V1.3.38 — Module Structure

## Quy tắc kiểm lỗi
Mọi lỗi UI đi theo chuỗi: Frontend event -> request/API -> Backend service -> Supabase/data -> template/view state -> DOM -> CSS.
Không sửa CSS để chữa lỗi dữ liệu và không sửa Backend khi DOM đã đúng nhưng chỉ bị style che.

## Presence
- Frontend: `static/js/presence.js`
- Backend: `modules/presence/service.py`
- Trách nhiệm: heartbeat, last_seen, quyết định online/offline.

## Invite
- Frontend: `static/js/invite_center.js`
- Backend: `modules/invites/service.py`
- Trách nhiệm: popup lời mời, pending/accept/reject, điều kiện gửi/nhận.

## Quick Match
- Frontend: `static/js/quick_match.js`
- Backend: `modules/quick_match/service.py`
- CSS: `static/css/quick_match.css`

## Rank Mode
- Backend catalog: `modules/rank_modes/catalog.py`
- Backend eligibility: `modules/rank_modes/service.py`
- Toggle/system rule: `modules/rank_mode_toggle/service.py`
- CSS: `static/css/rank_mode_toggle.css`

## Room UI
Room CSS không còn nằm trong một file 1.500+ dòng. Thứ tự load là hợp đồng cascade và được khai báo tại `templates/room_detail.html`.

1. `static/css/room/01-shell-layout.css` — khung phòng, grid, player cards, center stage.
2. `static/css/room/02-club-visuals.css` — CLB, stadium/branding visual.
3. `static/css/room/03-mode-selector.css` — bộ chọn chế độ Rank, neon mode cards, random presentation.
4. `static/css/room/04-actions-history.css` — nút hành động, xác nhận kết quả, lịch sử.
5. `static/css/room/05-action-states.css` — trạng thái ready/wait/result và visual state của action.
6. `static/css/room/06-responsive-performance.css` — responsive và giảm repaint/effect nặng.
7. `static/css/room/07-parsec-history-polish.css` — cân Parsec/history và lớp polish cuối.

`static/css/arena_room_v2.css` chỉ còn là compatibility index bằng `@import`, không phải nơi thêm rule mới.

## CSS ownership rule
- Rule Room mới phải bắt đầu bằng `.arena-room-v2`.
- Không thêm CSS Room mới vào `static/style.css`.
- Không dùng `!important` mới nếu selector module đủ specificity.
- Nếu cần override, sửa module sở hữu selector thay vì thêm block version mới ở cuối file.
- `display:none`, `visibility:hidden`, `opacity:0` phải được audit vì có thể che DOM dù Backend đúng.

## Tool audit
Chạy: `python scripts/audit_css_flow.py`
Báo cáo release: `docs/CSS_MODULE_AUDIT_V1.3.38.txt`.
