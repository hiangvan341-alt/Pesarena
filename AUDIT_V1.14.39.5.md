# Rà soát Collap V1.14.39.5

## Đã kiểm tra
- Cú pháp toàn bộ file Python bằng `compileall`.
- Các route trùng trong mã nguồn.
- Import/đăng ký module trong `app.py`.
- Module Zcoin, Điểm danh, Gift Code, Admin Economy và Profile.
- CSS chính, CSS Zcoin, CSS phần thưởng và CSS hiệu ứng chuỗi.
- Bố cục Admin desktop/mobile và khối hệ số RP gặp lại đối thủ.

## Đã sửa
- Xóa module Zcoin legacy không còn được đăng ký:
  - `modules/zcoin_routes.py`
  - `modules/zcoin_service.py`
  - `templates/zcoin_wallet.html`
- Xóa toàn bộ `__pycache__` và `.pyc` khỏi gói phát hành.
- Loại bỏ nguồn route trùng `/zcoin` và `/admin/zcoin/adjust` trong mã nguồn legacy.

## Kết luận module
- Zcoin mới: `modules/zcoin/`.
- Điểm danh: `modules/daily_checkin/`.
- Gift Code: `modules/gift_codes/`.
- Admin Economy: `modules/admin_economy/`.
- Profile: `modules/profile/`.
- Các module trên đã được đăng ký độc lập trong `app.py`.

## CSS
- Không phát hiện selector của khối hệ số RP mới ghi đè lên module khác vì đều dùng tiền tố `.repeat-rp-*`.
- Nhiều selector lặp trong `static/style.css` thuộc các breakpoint và các lớp vá phiên bản cũ; chưa nên tự động xóa vì có thể làm thay đổi giao diện phòng đấu/BXH.
- `zcoin.css` và `zcoin_rewards.css` dùng namespace riêng, rủi ro chồng thấp.

## Điểm còn nên tách ở phiên bản sau
- `templates/admin.html` vẫn là file lớn; nên tách từng tab thành `templates/admin/partials/`.
- `static/style.css` còn lớn; nên tách `room.css`, `ranking.css`, `admin.css` sau khi có kiểm thử giao diện từng trang.
- `app.py` vẫn chứa nhiều hàm lõi; không nên tách hàng loạt trong một lần vì rủi ro route và dependency.
