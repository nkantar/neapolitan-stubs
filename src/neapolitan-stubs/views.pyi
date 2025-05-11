"""Type stubs for Neapolitan. https://github.com/nkantar/neapolitan-stubs"""

import builtins
from enum import Enum
from typing import Any, Callable, Iterable, Literal, TypedDict, TypeVar

from django.core.paginator import Paginator
from django.db.models import Model
from django.db.models.base import ModelBase
from django.db.models.query import QuerySet
from django.forms.forms import BaseForm
from django.http import HttpRequest, HttpResponseBase, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import URLPattern, URLResolver
from django.utils.decorators import classonlymethod
from django.utils.functional import classproperty
from django.views import View
from django_filters.filterset import FilterSet


_M = TypeVar("_M", bound=Model)


class _RoleHandlersReturn(TypedDict):
    """Return type for Role.handlers."""

    get: Literal["get", "detail", "show_form", "confirm_delete"]
    post: Literal["process_form", "process_deletion"] | None


class _RoleExtraInitKwargsReturn(TypedDict):
    """Return type for Role.extra_initkwargs."""

    template_name_suffix = Literal["_list", "_detail", "_form", "_confirm_delete"]


class Role(Enum):
    LIST = "list"
    CREATE = "create"
    DETAIL = "detail"
    UPDATE = "update"
    DELETE = "delete"

    def handlers(self) -> _RoleHandlersReturn: ...

    def extra_initkwargs(self) -> _RoleExtraInitKwargsReturn: ...

    @property
    def url_name_component(self) -> str: ...

    def url_pattern(self, view_cls: View) -> str: ...

    def get_url(self, view_cls: View) -> URLPattern | URLResolver: ...

    def reverse(self, view: View, object: type[_M] | None) -> str: ...

    def maybe_reverse(self, view: View, object: type[_M] | None) -> str | None: ...


# ================================================


class CRUDView(View):
    role: Role
    model: type[_M] | None
    fields: list[str] | None

    lookup_field: str
    lookup_url_kwarg: str | None
    path_converter: str
    object: ModelBase | None

    queryset: QuerySet[_M] | None
    form_class: type[BaseForm] | None
    template_name: str | None
    context_object_name: str | None

    paginate_by: int
    page_kwarg: str
    allow_empty: bool

    template_name_suffix: str | None

    def list(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> TemplateResponse: ...

    def detail(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> TemplateResponse: ...

    def show_form(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> TemplateResponse: ...

    def process_form(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponseRedirect | TemplateResponse: ...

    def confirm_delete(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> TemplateResponse: ...

    def process_deletion(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponseRedirect: ...

    def get_queryset(self) -> QuerySet: ...

    def get_object(self) -> _M: ...

    def get_form_class(self) -> BaseForm: ...

    def get_form(self, data=None, files=None, **kwargs: Any) -> BaseForm: ...

    def form_valid(self, form: BaseForm) -> HttpResponseRedirect: ...

    def form_invalid(self, form: BaseForm) -> TemplateResponse: ...

    def get_success_url(self) -> str: ...

    def get_paginate_by(self) -> int: ...

    def get_paginator(self, queryset: QuerySet, page_size: int) -> Paginator: ...

    def paginate_queryset(self, queryset: QuerySet, page_size: int) -> Paginator: ...

    def get_filterset(self, queryset: QuerySet) -> FilterSet: ...

    def get_context_object_name(self, is_list: bool) -> str: ...

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

    def get_template_names(self) -> builtins.list[str]: ...

    def render_to_response(self, context: dict[Any, Any]) -> TemplateResponse: ...

    @classonlymethod
    def as_view(
        cls,
        role: Role,
        **initkwargs: Any,
    ) -> Callable[
        [HttpRequest, Any, Any],
        Callable[[HttpRequest, Any, Any], HttpResponseBase],
    ]: ...

    @classproperty
    def url_base(cls) -> str: ...

    @classonlymethod
    def get_urls(cls, roles: Iterable | None) -> Iterable[URLPattern | URLResolver]: ...
