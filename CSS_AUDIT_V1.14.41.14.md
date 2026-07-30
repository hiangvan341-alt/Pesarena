# CSS AUDIT V1.14.41.14

## Phạm vi đã kiểm tra
- `static/style.css`
- Toàn bộ `static/css/*.css`
- Thứ tự nạp CSS trong `templates/base.html`
- Các class được dùng trong template, JavaScript và Python

## Thay đổi an toàn đã thực hiện
1. Chuẩn hóa một font toàn dự án bằng biến `--app-font`.
2. Cho `button`, `input`, `select`, `textarea`, `option` kế thừa font chung.
3. Module Parsec không khai báo bộ font riêng nữa; dùng font toàn dự án.
4. Giữ thứ tự nạp: `style.css` trước, CSS module sau.
5. Xóa 5 rule `.tier-*` bị lặp nguyên vẹn.
6. Không xóa các selector chỉ “có vẻ không dùng” vì nhiều class được tạo theo trạng thái động; xóa tự động có thể làm hỏng phòng đấu, admin hoặc trạng thái RP.

## Kết quả rà soát
- `style.css` có nhiều selector được khai báo lại theo từng phiên bản. Phần lớn là override có chủ đích và phụ thuộc thứ tự cascade.
- Chỉ các rule trùng hoàn toàn mới được xóa trong bản này.
- Các font trang trí như `Impact` ở logo, cúp và hiệu ứng chuỗi thắng được giữ lại vì đó là typography trang trí, không phải font nội dung.
- CSS Parsec tiếp tục được cô lập bằng `.parsec-room-panel` và các class con.

## Nguyên tắc sau bản này
- Không thêm CSS vá vào cuối `style.css` nếu đã có selector tương ứng.
- Sửa tại section gốc hoặc file module riêng.
- Không dùng selector chung như `img`, `.btn`, `.panel` trong CSS module nếu không có class cha của module.
