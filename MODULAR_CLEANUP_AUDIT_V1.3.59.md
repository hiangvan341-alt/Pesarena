# PES Arena V1.3.59 — Modular Cleanup Audit

## Kết luận nhanh

| Khu vực | Trạng thái | Kết luận |
|---|---|---|
| `templates/room_detail.html` | PASS | Đã trở thành file orchestration 47 dòng. V1.3.59 sửa ranh giới HTML để partial không đóng thẻ của file cha và loại bỏ 1 `</div>` dư từ cấu trúc cũ. |
| `static/style.css` | WARNING | File entrypoint đã gọn còn 11 dòng, nhưng 6 module `static/css/legacy/*` vẫn là nợ kỹ thuật lớn; chưa thể gọi là “dọn sạch legacy”. |
| `app.py` | WARNING | Đã giảm từ 6.577 xuống 3.547 dòng (~46,1%) và core/routes/services đã tách đáng kể, nhưng vẫn còn 90 top-level function; chưa phải app bootstrap mỏng. |
| Black Box Safety API | PASS (source-level) | Route được bọc fail-safe JSON; frontend kiểm tra Content-Type/status trước parse để không còn lỗi mơ hồ `Unexpected token '<'`. |

## 1. room_detail.html

- V1.3.51: 1.596 dòng.
- V1.3.59: 47 dòng (~97,1% giảm).
- Layout, card, controls và JS đã chia qua `templates/room/*`.
- CSS phòng đã chia thành 9 module theo trách nhiệm.
- Sửa lỗi ownership trong V1.3.58:
  - `_extra_controls.html` trước đây đóng thêm 2 `</div>` thuộc file cha/legacy.
  - Sau sửa, `_extra_controls.html` tự cân bằng thẻ của chính nó.
  - `room_detail.html` tự đóng `#roomLiveShell`.
  - Khi expand các include tĩnh: `div 138/138`, `section 8/8`, `aside 2/2`, `form 29/29`.

## 2. style.css / legacy CSS

`static/style.css` hiện chỉ là compatibility entrypoint 11 dòng và không nên chứa CSS tính năng mới.

Tuy nhiên phần legacy thực tế vẫn còn:

- 6 file legacy.
- Tổng 5.326 dòng.
- 1.116 lần dùng `!important`.
- Hai file legacy room-generation vẫn chứa nhiều selector `.room-*` đang dùng.

Vì vậy **không nên xóa 04/06-room-generation ngay trong hotfix**. Cần một đợt cleanup riêng có visual regression/selector ownership test, nếu không dễ tái diễn lỗi giao diện chồng CSS.

Room CSS mới hiện có 1.806 dòng và 97 `!important`; đây cũng là khu vực nên tiếp tục giảm override sau khi production ổn định.

## 3. app.py

- V1.3.51: 6.577 dòng.
- V1.3.59: 3.547 dòng.
- Giảm khoảng 46,1%.
- Không còn duplicate function giữa `app.py` và các `EXPORTED_NAMES` đã tách.
- Core/service/route registrar đã tách đáng kể.

Nhưng `app.py` vẫn còn 90 top-level function. Các nhóm còn nên tách ở giai đoạn sau:

1. Auth/password/session guard.
2. Presence/session activity endpoints.
3. Lobby/global chat endpoints.
4. Invite/quick-match orchestration còn lại.
5. Page/read-model composition còn ở app.

Không tiếp tục tách các nhóm này trong V1.3.59 vì mục tiêu hotfix là ổn định startup + Safety API; lần modular hóa lớn trước đã cho thấy refactor nhiều dependency cùng lúc có rủi ro cao.

## 4. Safety API V1.3.59

Backend:

- `run_server_safety_audit()` được bọc `try/except` tại route.
- Khi audit lỗi, route vẫn trả JSON có `report.checks` thay vì trang HTML 500 chung của Flask.
- `Cache-Control: no-store` cho endpoint diagnostics.

Frontend:

- Không gọi `res.json()` mù nữa.
- Đọc `Content-Type`, HTTP status, redirect và response text trước.
- Nếu server trả HTML/redirect, report ghi rõ HTTP/status/content-type thay vì `Unexpected token '<'`.

## Nguyên tắc sau V1.3.59

- `room_detail.html`: chỉ orchestration/includes và biến template cấp trang.
- Partial chỉ đóng thẻ do chính partial mở.
- `style.css`: chỉ compatibility imports, không thêm rule mới.
- CSS tính năng mới đi vào module scoped.
- `app.py`: không kéo function đã tách ngược trở lại; mỗi đợt tách mới phải có import-time/binding regression test trước deploy.
