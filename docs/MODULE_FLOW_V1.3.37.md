# PES Arena V1.3.37 — Luồng dữ liệu & ranh giới Module

## Quy tắc kiểm tra lỗi

Mỗi lỗi giao diện phải được lần theo đúng thứ tự:

`Frontend Event -> Request/API -> Backend Decision -> Supabase Write/Read -> Backend View Model -> HTML DOM -> CSS Render`

CSS không được coi là nguyên nhân làm sai dữ liệu Backend. CSS chỉ có thể làm **DOM đúng nhưng hiển thị sai/ẩn/sai màu/sai kích thước**.

## Module 1 — Presence

- Frontend: `static/js/presence.js`
- Backend rule: `modules/presence/service.py`
- Route I/O còn ở `app.py`: `/heartbeat`, `/presence/offline`
- Nguồn dữ liệu: `users.is_online`, `users.last_seen_at`
- Contract: Online khi `is_online=true` và `last_seen_at` chưa quá 120 giây.

Kiểm tra lỗi:
1. DevTools Network có POST `/heartbeat` hay không.
2. Backend trả 200 hay lỗi.
3. Supabase `last_seen_at` có đổi hay không.
4. `is_user_online_now()` phải dùng duy nhất Presence service.
5. Players/Invite/Quick Match không được tự đặt timeout khác.

## Module 2 — Rank Invite

- Backend rule: `modules/invites/service.py`
- Route I/O: `/invites/send`, `/invites/respond/<id>`, `/api/invites/pending`
- Bảng dữ liệu: `match_invites`, `match_rooms`, `matches`, `users`

Luồng gửi:
`button Mời -> POST /invites/send -> matchmaking_snapshot -> send_invite_blocker -> insert match_invites -> create/attach match_rooms -> redirect room`

Luồng nhận:
`poll /api/invites/pending -> popup -> POST respond -> accept_invite_blocker -> attach guest -> accepted -> cancel invite khác -> redirect room`

## Module 3 — Quick Match

- Frontend: `static/js/quick_match.js`
- Backend rule: `modules/quick_match/service.py`
- Route I/O hiện ở `app.py`
- Presence bắt buộc dùng cùng `is_user_online_now()` / timeout 120 giây.

## Module 4 — Rank Modes

- Catalog: `modules/rank_modes/catalog.py`
- Eligibility/service: `modules/rank_modes/service.py`
- Toggle: `modules/rank_mode_toggle/service.py`
- CSS: `static/css/rank_mode_toggle.css`, phần room chính ở `arena_room_v2.css`

## Module 5 — Room UI

- Template chính: `templates/room_detail.html`
- Live partial: `templates/_room_live_content.html`
- CSS chính: `static/css/arena_room_v2.css`
- Parsec: `static/css/parsec_room.css`
- Quick Match UI: `static/css/quick_match.css`

`room_detail.html` và `_room_live_content.html` phải giữ cùng class/state. Nếu một bên có nút mà bên kia thiếu, polling live có thể làm giao diện “biến mất” sau lần refresh partial.

## CSS audit

Chạy:

`python scripts/audit_css_flow.py`

Audit kiểm tra:
- số lượng `!important`;
- selector exact trùng giữa nhiều file;
- selector lặp nhiều lần trong `arena_room_v2.css`;
- selector dùng `display:none`, `visibility:hidden`, `opacity:0` có thể che state UI.

### Legacy được ẩn có chủ đích

`.arena-room-v2 .room-center-mode-zone { display:none; }` hiện là UI cũ. Chế độ Rank mới dùng `.room-master-mode-switcher`. Không được tự bỏ `display:none` nếu chưa xóa HTML legacy.

## Quy tắc nâng cấp từ V1.3.37

1. Business rule không viết thêm trực tiếp vào CSS/JS.
2. Frontend chỉ gửi event và render state.
3. Backend service quyết định hợp lệ/không hợp lệ.
4. Route chỉ đọc request, gọi service, đọc/ghi DB và trả response.
5. CSS module phải scope theo component/page; tránh selector chung như `.btn`, `form button`, `small` trong module mới.
6. Không thêm `!important` nếu chưa ghi rõ selector đang cần thắng rule nào.
7. Mỗi bug mới phải có test cho service hoặc source contract trước khi đóng phiên bản.
