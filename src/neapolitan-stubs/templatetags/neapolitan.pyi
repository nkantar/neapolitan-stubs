"""Type stubs for Neapolitan templatetags. https://github.com/nkantar/neapolitan-stubs"""

from typing import Any, TypeVar
from django.db.models import Model
from django.template import Library
from django.utils.safestring import SafeString
from neapolitan.views import CRUDView

_ModelT = TypeVar("_ModelT", bound=Model)

register: Library

def action_links(view: CRUDView[_ModelT], object: _ModelT) -> SafeString: ...
def object_detail(object: _ModelT, fields: list[str]) -> dict[str, Any]: ...
def object_list(objects: list[_ModelT], view: CRUDView[_ModelT]) -> dict[str, Any]: ...
