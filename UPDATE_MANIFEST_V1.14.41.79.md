# PES Arena V1.14.41.79 — Room Result Confirmation Reliability Fix

## Cơ sở phiên bản

- Bản full source được kiểm tra: `Pesarenahiang-main (2).zip`.
- `app.py` trong bản full source đang là `V1.14.41.77`.
- Trạng thái Preview `V1.14.41.78` được tái tạo bằng cách áp đúng hai file runtime từ patch `PES_ARENA_V1.14.41.78_ROOM_SESSION_GUARD_FIX_PATCH_ONLY(2).zip` lên bản full source:
  - `app.py`
  - `static/js/session-timeout.js`
- Patch này phải được áp trên branch đang có `V1.14.41.78`.

## Nguyên nhân gốc đã xác nhận

`modules/match_result_service.py` gọi:

```python
get_win_streak_bonus(player1, score1 > score2)
get_win_streak_bonus(player2, score2 > score1)
```

nhưng module không import hàm này và `app.py` cũng không đưa `get_win_streak_bonus` vào context khi gọi `configure(globals())`.

Khi khách bấm **Xác nhận**, `apply_match_result()` chạy và phát sinh lỗi thực tế:

```text
NameError: name 'get_win_streak_bonus' is not defined
```

Lỗi bị `room_confirm_result()` bắt bởi nhánh `except Exception`, sau đó hiển thị thông báo chung:

> Không thể xác nhận kết quả do lỗi kết nối dữ liệu...

Đây không phải lỗi kết nối Supabase được chứng minh; thông báo frontend đã che mất lỗi `NameError` phía Python.

## Vì sao chỉ xuất hiện khi xác nhận tỷ số

- Chủ phòng gửi tỷ số chỉ lưu `matches` và `match_rooms`; chưa gọi bộ máy tính RP.
- Khách bấm xác nhận mới gọi `apply_match_result()`.
- Hàm bị thiếu chỉ được gọi bên trong luồng tính RP của `apply_match_result()`.
- Vì vậy việc vào phòng, Ready, bắt đầu trận và gửi tỷ số vẫn có thể hoạt động; lỗi xuất hiện tại bước xác nhận.

## Quan hệ với V1.14.41.78

- V1.14.41.78 chỉ thay đổi bảo vệ session trong `app.py` và `static/js/session-timeout.js`.
- Không sửa `modules/match_result_service.py` hoặc `modules/room_result_routes.py`.
- Hotfix session không trực tiếp tạo ra lỗi `NameError`.
- Lỗi đã tồn tại trong source V1.14.41.77 và được phát hiện khi kiểm tra Preview V1.14.41.78.
- Toàn bộ cơ chế giữ session 4 giờ khi đang thi đấu của V1.14.41.78 được giữ nguyên.

## Thay đổi runtime

### `app.py`

- Tăng `APP_VERSION` từ `V1.14.41.78` lên `V1.14.41.79`.
- Không thay đổi route, Profile V2, Shop, Lucky Box, Inventory, Zcoin, Gift Code, BXH hoặc Admin.

### `modules/match_result_service.py`

- Import trực tiếp `random` trong module thay vì chỉ phụ thuộc context từ `app.py`.
- Import trực tiếp `get_win_streak_bonus` từ `modules.rp_engine`.
- Không thay đổi công thức RP, hệ số chủ phòng, giới hạn RP ngày, quy tắc gặp lại đối thủ hoặc logic idempotency.

## File kiểm thử

### Test mới

- `test_room_result_confirmation_reliability_v1144179.py`
- `test_room_result_routes_v1144179.py`

### Test phiên bản được cập nhật

- `test_ip_random_session_v1144163.py`
- `test_luckybox_admin_source.py`
- `test_luckybox_core_source.py`
- `test_luckybox_user_ui_source.py`
- `test_profile_arena_overview_v1144175.py`
- `test_profile_badge_room_kick_source.py`
- `test_profile_empty_banner_clean_v1144177.py`
- `test_profile_full_bleed_banner_v1144176.py`
- `test_profile_showcase_v1144169.py`
- `test_profile_summoner_identity_v1144174.py`
- `test_remember_admin_accounts_v1144162.py`
- `test_room_guest_visibility_v1144166.py`
- `test_room_session_guard_v1144178.py`
- `test_total_matches_source_of_truth.py`
- `test_v1144167_room_daily_limit.py`

Các file trên chỉ đổi mốc `APP_VERSION` mong đợi sang `V1.14.41.79`; không đổi điều kiện hồi quy của tính năng.

## Những phần không bị ảnh hưởng

- Profile V2 và banner full-bleed.
- Shop, Inventory, Lucky Box.
- Zcoin, Gift Code, Daily Check-in.
- BXH, công thức RP và giới hạn trận/RP ngày.
- Admin và quyền Admin.
- Kick người chơi, giới hạn phòng và Quick Match.
- Session timeout thông thường 60 phút ngoài phòng.
- Session guard 4 giờ trong phòng của V1.14.41.78.

## Database / SQL

- Không cần SQL.
- Không thay đổi bảng, cột, constraint, RPC hoặc dữ liệu Supabase.

## Rủi ro còn lại

- Mức rủi ro của patch: thấp; thay đổi runtime chỉ là import dependency bị thiếu và tăng phiên bản.
- Kiểm thử trong sandbox không kết nối Supabase thật và không khởi chạy Flask server vì môi trường không có package Flask/Supabase và không có thông tin kết nối.
- Cơ chế ghi RP hiện tại vẫn là nhiều lệnh Supabase tuần tự, không phải một transaction SQL duy nhất. Idempotency chống bấm lặp đã được kiểm tra bằng unit test, nhưng lỗi mạng đúng giữa hai lệnh cập nhật người chơi cần tiếp tục được quan sát trong Preview/live logs.

## Rollback

1. Khôi phục `app.py` về bản V1.14.41.78.
2. Khôi phục `modules/match_result_service.py` về bản trước patch.
3. Các file test và hai báo cáo có thể xóa mà không ảnh hưởng runtime.

Không cần rollback database.
