# PES Arena — Logging guide

## Runtime output

Production/serverless logs are written to stdout so Vercel captures them. Local development can also write rotating files to `logs/pes_arena.log`.

Environment variables:

| Variable | Default | Purpose |
|---|---|---|
| `PES_LOG_LEVEL` | `INFO` | INFO / WARNING / ERROR |
| `PES_SLOW_REQUEST_MS` | `1500` | requests above this become `slow_request` |
| `PES_LOG_TO_FILE` | dev/test=on, production=off | enable local rotating log file |
| `PES_LOG_FILE` | `logs/pes_arena.log` | custom local log path |

## Events to search first

| Event | Meaning |
|---|---|
| `request_complete` | normal request with status + duration |
| `slow_request` | request exceeded slow threshold |
| `database_query_retry` | transient Supabase/network failure; retry started |
| `database_query_failed` | Supabase query failed after retry policy |
| `uncaught_exception` | unhandled backend exception with traceback in logger |
| `application_logging_ready` | logging initialized at process start |

## Error workflow

1. Reproduce the problem and copy the `X-Request-ID` response header from Network/DevTools when possible.
2. Search Vercel/local logs for that request ID.
3. Read `endpoint`, `status`, `duration_ms`, and any neighboring DB/error event.
4. Fix the owning module from `docs/MODULE_ARCHITECTURE_V1.3.52.md` rather than patching unrelated CSS/route code.
5. Add a regression test and note the request/event in `Log.md`.

Do not log passwords, session cookies, Parsec secrets, Supabase keys, full authorization headers, or uploaded evidence bytes.
