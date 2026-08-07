# PES Arena V1.3.47 — Audit luồng 6 chế độ Rank

## 1. Nguồn dữ liệu chuẩn

`Admin -> rank_mode_configs_v1 -> match_rooms.team_tier -> normalize_rank_mode_code() -> selected_rank_mode -> UI/route`

- Admin chỉ bật/tắt và cấu hình điều kiện/công thức cho 6 `mode_code`.
- Phòng lưu mode đang chọn tại `match_rooms.team_tier` (legacy `smart_random` được chuẩn hóa thành `rank_random`).
- Frontend không được tự đoán mode từ `rank_standard_enabled` hoặc từ tên nút.
- Nhãn/logo/thông tin phòng phải đọc cùng `selected_rank_mode`.

## 2. Kết quả kiểm tra từng chế độ

| mode_code | Hiển thị tên/logo | Chọn từ phòng | Luồng bắt đầu trận | Kết luận V1.3.47 |
|---|---|---|---|---|
| `rank_random` | OK | OK | `room_random_teams` | Hoạt động |
| `random3_pick1` | OK | OK | `room_start_random3_friendly` + chọn 1/3 | Hoạt động |
| `home_away` | Đã sửa | OK nếu đủ điều kiện | Chưa có bộ điều phối 2 lượt hoàn chỉnh | Không cho rơi nhầm sang Rank thường |
| `bo3` | Đã sửa | OK nếu đủ điều kiện | Chưa có bộ điều phối trận con hoàn chỉnh | Không cho rơi nhầm sang Rank thường |
| `tactical_bo3` | Đã sửa | OK nếu đủ điều kiện | Chưa có bộ điều phối 3 CLB/không lặp hoàn chỉnh | Không cho rơi nhầm sang Rank thường |
| `ban_pick_bo3` | Đã sửa | OK nếu đủ điều kiện | Chưa có luồng ban/pick + trận con hoàn chỉnh | Không cho rơi nhầm sang Rank thường |

## 3. Lỗi tìm thấy

### A. Nhãn phòng bị rút gọn sai
`app.py/enrich_room()` trước đây chỉ phân biệt `random3_pick1` và phần còn lại. Vì vậy `home_away`, `bo3`, `tactical_bo3`, `ban_pick_bo3` đều có thể hiện thành `Xếp hạng (Rank)`/Rank thường.

**Đã sửa:** lấy label trực tiếp từ `get_rank_mode(selected_rank_mode)`.

### B. Route quay quân có thể ghi đè mode
`room_random_teams()` là luồng Rank thường nhưng trước đây nhận cả mode Series rồi cuối route ghi `team_tier = smart_random`. Nếu một UI cũ/polling fragment mở nút này cho Series, mode bị đổi về Rank thường.

**Đã sửa:** route chỉ nhận `rank_random`; mode khác bị chặn rõ ràng, không ghi đè dữ liệu.

### C. Hai template không đồng nhất
`room_detail.html` đã chặn nút Series nhưng `_room_live_content.html` vẫn có đường rơi xuống `room_random_teams()` và dùng trực tiếp `room.team_tier`.

**Đã sửa:** cả hai cùng dùng `selected_rank_mode`, cùng guard Series.

### D. CSS chồng nút
Các module 03/04/05 cùng sở hữu selector `room-center-primary-actions`, `room-action-zone`, `room-center-random-form`. Trong 05 có `left:50%`, `bottom`, `transform:translateX(-50%)` áp lên phần tử vẫn ở `position:relative`, trong khi các block Quay quân/Thoát phòng cùng nằm trong flow cố định 535–548px. Đây là nguyên nhân trực tiếp khiến nút chồng nhau khi trạng thái thay đổi.

**Đã sửa:** module cuối `08-action-layout-guard.css` trả các action về normal flow (`left/right/bottom:auto`, `transform:none`) và compact riêng `waiting_ready`.

## 4. Điểm còn tồn tại cần tách tiếp

CSS audit cho thấy dự án vẫn còn nhiều selector Room bị sở hữu chéo giữa 01/03/04/05/06/07. V1.3.47 dùng module 08 làm guard an toàn, chưa xóa hàng loạt rule cũ để tránh làm hỏng các trạng thái khác. Khi refactor tiếp nên gom quyền sở hữu như sau:

- `01-shell-layout.css`: chỉ grid/kích thước/khung.
- `03-mode-selector.css`: chỉ thẻ mode + logo mode.
- `04-actions-history.css`: history + style chung button.
- `05-action-states.css`: màu/trạng thái button, không định vị.
- `08-action-layout-guard.css`: sau khi ổn định có thể nhập ngược vào 01/05 rồi xóa guard.

## 5. Luồng chuẩn từ Admin tới phòng

1. Admin bật/tắt 6 mode -> lưu `rank_mode_configs_v1`.
2. Người chơi vào phòng -> backend dựng `rank_mode_catalog_for_players()` theo enabled + RP + số trận + chênh RP + quota ngày.
3. Chủ phòng chọn mode -> POST `/room/<id>/select-ranked-mode`.
4. Backend validate lại -> lưu đúng `team_tier/mode_code` vào phòng.
5. `build_room_template_context()` chuẩn hóa thành `selected_rank_mode`.
6. Tên/logo/mô tả/nút bắt đầu đều đọc từ `selected_rank_mode`.
7. Khi bắt đầu trận, route chuyên biệt phải xác nhận đúng mode; không route nào được tự fallback sang `rank_random`.
