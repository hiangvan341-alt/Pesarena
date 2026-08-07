# Series Daily Quota V1.3.46

Quota tối thiểu trước khi bắt đầu:
- rank_random: 1
- random3_pick1: 1
- home_away: 2
- bo3: 3
- tactical_bo3: 3
- ban_pick_bo3: 3

Nguyên tắc:
1. Bắt đầu Series mới: kiểm tra RP/min_matches và đủ quota tối đa của mode.
2. Series đã bắt đầu (`__RANK_MODE_LOCKED__`): không kiểm tra lại RP/min_matches; mỗi game tiếp theo chỉ cần còn 1 quota thực tế.
3. Quota được đếm từ bảng matches như trước. BO3 2-0 tạo 2 match => dùng 2 lượt; BO3 2-1 tạo 3 match => dùng 3 lượt.
4. Nếu một trong hai người không đủ quota tại thời điểm bắt đầu, mode bị khóa cho phòng.
