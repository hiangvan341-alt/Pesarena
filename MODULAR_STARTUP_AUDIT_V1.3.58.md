# PES Arena V1.3.58 — Modular Startup Audit

## Regression chain found

1. V1.3.52: `list_user_devices.last_status` remained in `app.py` before core binding.
2. V1.3.52: app-owned constants were evaluated in extracted module default arguments at import time.
3. V1.3.53+: Black Box package declared service `EXPORTED_NAMES` but did not expose those functions on `modules.blackbox`, while `app.py` binds exports from the package object.

## Fix in V1.3.58

`modules/blackbox/__init__.py` now follows the same facade contract used by Zcoin/Daily Check-in/Gift Codes: configure the service, re-export every `EXPORTED_NAMES` member, and expose `register_routes`.

## Guard tests

- `test_core_startup_binding_regression.py`
- `test_core_import_time_dependencies.py`
- `test_service_binding_exports.py`

These tests target startup/import regressions caused by module extraction rather than gameplay behavior.
