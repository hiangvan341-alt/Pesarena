# TEST REPORT — PES Arena V1.14.41.79

## Ngày kiểm tra

- 2026-08-03

## Kết quả tổng hợp

| Hạng mục | Kết quả thực tế |
|---|---:|
| Toàn bộ pytest trong source | **135 passed / 0 failed** |
| Test tập trung session + xác nhận kết quả | **13 passed / 0 failed** |
| Jinja template parse | **48 parsed / 0 errors** |
| Python compile | **PASS** |
| JavaScript syntax `session-timeout.js` | **PASS** |
| SQL migration | **Không cần** |

## Lệnh đã chạy

```text
pytest -q --disable-warnings
```

Kết quả:

```text
135 passed in 0.39s
```

```text
pytest -q test_room_result_routes_v1144179.py \
          test_room_result_confirmation_reliability_v1144179.py \
          test_room_session_guard_v1144178.py
```

Kết quả:

```text
13 passed in 0.14s
```

Ngoài ra đã chạy:

```text
python -m compileall -q app.py modules *.py
node --check static/js/session-timeout.js
```

và parse toàn bộ 48 template bằng Jinja2.

## Bằng chứng tái hiện nguyên nhân V1.14.41.78

Khi chạy `apply_match_result()` với đúng context mà `app.py` cung cấp, trước khi sửa nhận được:

```text
apply_match_result ERROR match=m1 status=waiting_confirm: NameError: name 'get_win_streak_bonus' is not defined
NameError: name 'get_win_streak_bonus' is not defined
```

Điều này xác nhận lỗi server là dependency Python bị thiếu, không phải bằng chứng của lỗi mạng Supabase.

## Các tình huống đã kiểm tra

### A. Session

- `ROOM_MATCH_INACTIVITY_TIMEOUT_SECONDS` vẫn bằng 4 giờ.
- Request `/room/` và `/api/room/` vẫn làm mới `last_real_activity`.
- Trang phòng vẫn giữ session khi tab nằm nền.
- Quy tắc timeout 60 phút ngoài phòng vẫn còn trong `session_runtime_service.py`.

### B. Xác nhận kết quả

- Chủ phòng gửi tỷ số thành công trong route harness.
- Trận chuyển sang `waiting_confirm`; phòng chuyển sang `waiting_result_confirm`.
- Khách xác nhận thành công và phòng trở về `waiting_ready`.
- Chủ phòng không được xác nhận thay khách; bộ máy RP không được gọi.
- Trường hợp khách báo sai tỷ số đi vào luồng tranh chấp, chưa áp dụng RP.
- Match đã `confirmed` trả kết quả idempotent và không ghi RP lần hai.
- Đường thành công gọi cập nhật hai người chơi đúng một lần và finalize match đúng một lần.
- Cơ chế claim `processing_result` tiếp tục được giữ nguyên.

### C. Response frontend

Route xác nhận hiện tại là form HTML POST, không phải API JSON:

```text
POST /room/<room_id>/confirm-result
```

Frontend mong đợi redirect về `room_detail` và đọc Flask flash. Vì vậy response đúng của route hiện tại là redirect + flash, không phải JSON. Thông báo trong ảnh được tạo từ nhánh flash lỗi của server.

### D. Hồi quy

Các test nguồn hiện có cho những phần sau đều đạt:

- Profile V2.
- Shop, Inventory và Lucky Box.
- Zcoin/Gift Code liên quan tới source registration.
- Admin route/module registration.
- Room badge/kick.
- Daily Rank limit.
- Total matches source of truth.
- Remember account và session/IP logic.

## Giới hạn kiểm thử

Không thực hiện được trong sandbox:

- Khởi chạy Flask server thật.
- Kết nối Supabase thật.
- Gọi Vercel Preview thật.
- Fault injection giữa các lệnh cập nhật Supabase.

Lý do: sandbox không có package Flask/Supabase, không có package index để cài dependency và không có biến môi trường kết nối dự án. Vì vậy trạng thái Preview phải được kiểm tra tiếp sau khi áp patch lên branch.

## Kết luận

- Nguyên nhân `NameError` đã được tái hiện trước sửa.
- Regression test mới chạy qua sau sửa.
- Không có test nào thất bại trong bộ 135 test nguồn hiện có.
- Chưa được coi là sẵn sàng Promote cho tới khi hai tài khoản thật kiểm tra xác nhận tỷ số trên Vercel Preview.
