# PES Arena V1.3.31 — Báo cáo rà soát module

## 1. Module Core nên giữ

- `modules/rank_modes/`: nguồn chuẩn cho danh sách 6 chế độ, điều kiện mở khóa, quyền mở riêng và công thức RP Series.
- `modules/rank_mode_toggle/`: lớp tương thích cho hai cờ Rank cũ. Chỉ nên dùng để tương thích route cũ, không nên tiếp tục thêm logic mới tại đây.
- `modules/admin_dashboard_routes.py`: trang tổng hợp Admin và cấu hình Rank.
- `modules/admin_system_routes.py`: bật/tắt tính năng hệ thống và 6 chế độ Rank.
- `modules/admin_player_routes.py`: thao tác trực tiếp với tài khoản người chơi.
- `modules/room_*_routes.py`: tách đúng theo truy cập phòng, quay đội, kết quả và đá tiếp.

## 2. Module CSS/JS nên giữ riêng

- `static/css/admin_dashboard.css`: chỉ chứa giao diện Admin.
- `static/js/admin_dashboard.js`: chỉ quản lý tab, bộ lọc user và lazy iframe Admin.
- `static/css/ui_dialog.css` + `static/js/ui_dialog.js`: thông báo, xác nhận và toast dùng chung toàn hệ thống.
- `static/css/arena_room_v2.css`: chỉ áp dụng cho phòng đấu V2.

## 3. Các điểm chồng chéo đã xử lý

1. **Listener tab Admin bị tạo lặp**: `pointerdown` từng được đăng ký bên trong `activateAdminTab()`. Mỗi lần đổi tab lại thêm listener mới, làm click càng lúc càng chậm. Đã thay bằng một listener duy nhất.
2. **Bật/tắt chế độ Rank xuất hiện ở hai nơi**: trước đây vừa nằm trong Quản lý chế độ Rank vừa nằm trong Hệ thống. Đã chuyển toàn bộ công tắc về Hệ thống.
3. **Mở khóa chế độ theo tài khoản nằm sai tab**: đã chuyển vào chi tiết từng người dùng.
4. **Thông báo trình duyệt và thông báo giao diện dùng lẫn nhau**: đã bổ sung module dialog/toast dùng chung và tự chuyển các `confirm()` khai báo trong template sang modal giao diện.
5. **Hai lớp cờ Rank cũ và cấu hình 6 mode mới**: vẫn cần giữ cờ cũ để route cũ hoạt động, nhưng nguồn chuẩn bật/tắt hiện là `rank_mode_configs_v1`.

## 4. Module chưa phù hợp, nên xử lý ở bản sau

### A. `admin.html` vẫn quá lớn

File này chứa tất cả tab Admin nên HTML tải ban đầu nặng dù panel đang ẩn. Nên tách thành:

- `templates/admin/overview.html`
- `templates/admin/users.html`
- `templates/admin/rooms.html`
- `templates/admin/matches.html`
- `templates/admin/rank_modes.html`
- `templates/admin/system.html`

Sau đó tải từng tab bằng endpoint JSON/HTML fragment. Đây là bước giúp giảm thời gian mở `/admin` rõ nhất.

### B. Route `/admin` vẫn tải nhiều dữ liệu cùng lúc

Hiện trang tải user, phòng, lời mời, trận, báo cáo, log và nhiều cấu hình trong một request. Nên chuyển các tab nặng sang endpoint riêng:

- `/admin/api/users`
- `/admin/api/matches`
- `/admin/api/match-report`
- `/admin/api/logs`

Tab chỉ gọi endpoint khi được mở lần đầu.

### C. `rank_mode_toggle` là lớp tương thích cũ

Module này chỉ biết `Rank thường` và `Random 3 chọn 1`, trong khi hệ thống đã có 6 chế độ. Không nên thêm tính năng mới vào module này. Khi toàn bộ route phòng đã đọc trực tiếp `rank_modes.service`, có thể loại bỏ lớp cũ.

### D. CSS phòng đấu có nhiều lớp vá theo phiên bản

`arena_room_v2.css` đang chứa nhiều block V1.3.20–V1.3.30 ghi đè nhau. Nên gom lại thành:

- `arena_room_layout.css`
- `arena_room_buttons.css`
- `arena_room_modes.css`
- `arena_room_history.css`
- `arena_room_responsive.css`

Sau khi tách, xóa các block cũ bị ghi đè để giảm kích thước CSS và chi phí tính style.

## 5. Luồng quản trị sau V1.3.31

- **Quản lý người dùng** → mở một người chơi → chỉnh thông tin, RP, mật khẩu và quyền mở 6 chế độ.
- **Quản lý chế độ Rank** → chỉ chỉnh điều kiện RP, số trận, chênh RP và công thức RP.
- **Hệ thống** → bật/tắt 6 chế độ và các tính năng chung.
- **Dialog dùng chung** → không dùng cửa sổ xác nhận mặc định của trình duyệt cho các form khai báo trong template.
