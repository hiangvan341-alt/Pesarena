"""Module Gift Code Zcoin cho member và Admin."""

from .service import EXPORTED_NAMES
from . import service as _service
from . import repository as _repository
from . import admin as _admin
from .routes import register_routes


def configure(context):
    _repository.configure(context)
    enriched = dict(context)
    for name in EXPORTED_NAMES:
        enriched[name] = getattr(_service, name)
    _service.configure(enriched)
    _admin.configure(enriched)


def build_admin_context(actor):
    return _admin.build_admin_context(actor)


for _name in EXPORTED_NAMES:
    globals()[_name] = getattr(_service, _name)

__all__ = ("configure", "register_routes", "build_admin_context", *EXPORTED_NAMES)
