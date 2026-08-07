# PES Arena V1.3.52 — Module Architecture

## 1. `room_detail.html`

`templates/room_detail.html` is now the room page orchestrator only. It owns page-level CSS imports, room context flags, and include order.

| Module | Responsibility |
|---|---|
| `templates/room/_topbar.html` | room title, code, PES Arena brand, share link |
| `templates/room/_host_card.html` | host player / club presentation |
| `templates/room/_center_stage.html` | active mode, Series panel, score/result/actions/random flow |
| `templates/room/_guest_card.html` | guest player / club / ready / kick presentation |
| `templates/room/_side_rail.html` | room info, Parsec, room chat shell |
| `templates/room/_bottom_modes_history.html` | mode switcher + room history |
| `templates/room/_extra_controls.html` | friendly/forfeit/dispute/completed states |
| `templates/room/_action_modal.html` | reusable room confirmation dialog |
| `templates/room/scripts/_room_runtime.html` | room state polling, async forms, timers, share link |
| `templates/room/scripts/_room_chat.html` | room chat polling / rendering / submit |
| `templates/room/scripts/_room_dialogs.html` | exit/confirm/notice modal behavior |

Rule: a new room feature must be added to the smallest matching partial; do not grow `room_detail.html` again.

## 2. CSS

`static/style.css` is now only an ordered compatibility entrypoint. Historical rules are frozen into six files under `static/css/legacy/` in the exact original cascade order.

New CSS must go into a scoped feature module such as `static/css/room/`, `static/css/admin/`, `static/css/profile/`, etc. Do not append new selectors to legacy files unless fixing a regression in a legacy page.

## 3. `app.py`

The monolith was reduced by extracting runtime/service responsibilities into `modules/core/` while preserving public function names for compatibility with existing route modules.

| Core module | Responsibility |
|---|---|
| `achievements.py` | achievement progress / sync / decoration |
| `rank_team_service.py` | rank ranges, team loading, Smart Random, tier selection |
| `room_runtime.py` | room expiry, timeout, room read model, room enrichment |
| `user_repository.py` | user/player/device/admin account reads and helpers |
| `match_repository.py` | matches, disputes, invites, match view decoration |
| `social_runtime.py` | announcements, streak events, chat data |
| `matchmaking_runtime.py` | active room/match checks, busy state, matchmaking snapshot |

`app.py` remains the Flask bootstrap + request hooks + high-level public/auth/invite routes. Future releases should migrate remaining route groups into blueprints one group at a time, with tests before removal.

## 4. Logging

`modules/observability/app_logging.py` provides structured JSON-lines logs for request timing, slow requests, DB retry/failure, and uncaught exceptions. Every request receives an `X-Request-ID` response header for tracing frontend reports to backend logs.
