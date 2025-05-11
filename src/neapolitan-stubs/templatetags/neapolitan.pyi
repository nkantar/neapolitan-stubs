"""Type stubs for Neapolitan. https://github.com/nkantar/neapolitan-stubs"""

from typing import Any, Iterable, TypeVar, TypedDict

from django.db.models import Model
from django.utils.safestring import SafeString
from django.views import View


_M = TypeVar("_M", bound=Model)


class ObjectDetail(TypedDict):
    object: tuple[str, str]


class ObjectListEntry(TypedDict):
    object: type[_M]
    fields: list[str]
    actions: SafeString


class HeadersAndObjectList(TypedDict):
    headers: Iterable[str]
    object_list: list[ObjectListEntry]


register: Any


def action_links(view: View, object: type[_M]) -> SafeString: ...


@register.inclusion_tag("neapolitan/partial/detail.html")
def object_detail(object: type[_M], fields: Iterable[str]) -> ObjectDetail: ...


@register.inclusion_tag("neapolitan/partial/list.html")
def object_list(objects: type[_M], view: View) -> HeadersAndObjectList: ...
