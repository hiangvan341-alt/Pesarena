# PES Arena V1.3.51 — System Inspection

## Kết luận nhanh
- Đã bổ sung watchdog cho Cấm chọn BO3: hết giờ cấm -> random 1 CLB để cấm; hết giờ chọn -> random 1 CLB hợp lệ.
- Đã dùng optimistic update theo `match_series.updated_at` để giảm double-action khi hai client poll cùng lúc.
- Đã sửa Tactical BO3 để toàn bộ CLB đã từng xuất hiện trong 3 lựa chọn không xuất hiện lại trong Series.
- Đã chặn cấu hình Ban/Pick không khả thi: pool tối thiểu = 2 x bans_per_player + 6.
- Đã bổ sung permission cho Admin sửa Rank mode và mở khóa mode người dùng.

## Điểm cấu trúc
| Module | Điểm | Kết luận |
|---|---:|---|
| App bootstrap / dependency wiring | 6.5/10 | Hoạt động nhưng `app.py` còn 6.5k dòng, vẫn là điểm nghẽn kiến trúc. |
| Room access / room lifecycle | 8.0/10 | Đã tách route; polling nhẹ. Route vẫn khá lớn. |
| Room team / random | 8.0/10 | Luồng rõ, cần tiếp tục giảm logic legacy trong route. |
| Match result / confirm / dispute | 8.0/10 | Có guard trạng thái; nhiều ghi DB liên tiếp chưa transaction. |
| Rank modes | 9.0/10 | Catalog + service rõ, Admin cấu hình tập trung. |
| Series orchestrator | 8.5/10 | 4 mode đầy đủ; rủi ro còn lại là transaction đa bảng khi chốt RP. |
| Home/Away | 8.5/10 | 2 lượt + aggregate + RP cuối Series đầy đủ. |
| BO3 | 9.0/10 | 2 thắng trước, tối đa 3 trận, không tái dùng CLB. |
| Tactical BO3 | 9.0/10 | 3 lựa chọn/người/trận; V1.3.51 chặn tái xuất hiện cả CLB không được chọn. |
| Ban/Pick BO3 | 9.0/10 | Pool chung, cấm/chọn, no-reuse, timeout random, chống double timeout. |
| RP engine / formula | 8.0/10 | Tách tốt; Series RP một lần. Chưa atomic khi cập nhật 2 người + series. |
| Daily quota / repeat opponent | 8.5/10 | Module riêng, có test và continuation Series. |
| Presence / invites / quick match | 8.5/10 | Tách module tốt, polling/single-flight hợp lý. |
| Read model / cache | 8.5/10 | Giảm tải Supabase tốt; phụ thuộc SQL migration. |
| Admin | 8.0/10 | Tab tách tốt; V1.3.51 bổ sung permission. Thiếu chi tiết Series trực tiếp ở tab Rooms. |
| Zcoin / Economy | 8.0/10 | Tách module; cần tiếp tục giữ audit log chặt với mọi mutation. |
| Shop / Inventory / LuckyBox | 8.0/10 | Module hóa khá tốt; bộ test cũ còn tham chiếu SQL đã loại bỏ. |
| Parsec room | 8.5/10 | Phạm vi nhỏ, tách service/route tốt. |
| Frontend Room | 6.5/10 | `room_detail.html` ~1.6k dòng; cần tiếp tục tách JS/template partial. |
| CSS | 6.0/10 | Đã có module CSS nhưng `static/style.css` vẫn ~5.3k dòng. |
| Test suite | 6.5/10 | Test lõi mới tốt nhưng toàn bộ suite còn test legacy/stale và asset/doc đã chuyển Supabase. |

## Sai sót / thiếu thông tin còn lại
| Mức | Khu vực | Vấn đề | Khuyến nghị |
|---|---|---|---|
| Cao | Series RP finalization | Update RP player1, player2, match, series là nhiều request DB, không phải transaction duy nhất. | Chuyển finalization sang Supabase RPC transaction. |
| Trung bình | Admin Rooms | Chưa hiển thị rõ mode hiện tại, series_id, game_no/phase. | Thêm cột Chế độ + Series/Trận + phase. |
| Trung bình | Admin Reports | Chưa thống kê số lượt `ban_auto` / `pick_auto` do timeout. | Thêm metric timeout auto-action. |
| Trung bình | Frontend | Room template và JS inline còn quá lớn. | Tách `room_live.js`, `room_series.js`, `room_result.js`. |
| Trung bình | CSS | style.css legacy còn lớn, nguy cơ cascade chéo. | Di chuyển dần selector phòng/admin sang scoped CSS module. |
| Thấp | Tests | Một số test kiểm tra version cũ, asset local cũ, SQL LuckyBox cũ. | Archive test legacy hoặc cập nhật theo Supabase asset pipeline hiện tại. |

## Kiểm tra V1.3.51
- 30 test mục tiêu: PASS.
- `py_compile`: PASS cho app + Series + Admin sửa đổi.
- Full pytest hiện không thể dùng làm tiêu chuẩn release vì collection còn 3 lỗi legacy: asset room local đã bỏ và 2 SQL LuckyBox cũ không còn trong project.
