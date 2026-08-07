# PES Arena Runtime Logs

Runtime log dùng định dạng **JSON Lines (JSONL)**: mỗi dòng là một JSON event độc lập.

Ví dụ:

```json
{"ts":"2026-08-08T01:00:00+00:00","level":"INFO","event":"request_complete","request_id":"abc123","method":"GET","path":"/ranking","endpoint":"ranking","status":200,"duration_ms":81.2}
```

## Cách tìm lỗi nhanh

1. Ưu tiên search theo `request_id`.
2. Nếu không có request ID, search theo `event` + `endpoint`.
3. `ERROR` → xem `error_type` + `error`.
4. `slow_request` → xem `duration_ms`, rồi tra module trong `PROJECT_MAP.md`.

## File

- Mặc định local: `logs/pes_arena.log`
- Rotate: tối đa 2 MB/file, giữ 5 bản backup.
- Production Vercel: stdout, không phụ thuộc file local.

Chi tiết: `docs/LOGGING_GUIDE_V1.3.61.md`.
