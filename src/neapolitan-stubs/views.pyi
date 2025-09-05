"""Type stubs for Neapolitan views. https://github.com/nkantar/neapolitan-stubs"""

from __future__ import annotations

import builtins
import enum
from collections.abc import Callable
from typing import Any, Generic, TypeVar
from django.core.paginator import Page, Paginator
from django.db.models import Model, QuerySet
from django.forms import ModelForm
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBase,
    HttpResponseRedirect,
)
from django.template.response import TemplateResponse
from django.urls import URLPattern
from django.utils.functional import classproperty
from django.views.generic import View
from django_filters.filterset import BaseFilterSet

_ModelT = TypeVar("_ModelT", bound=Model)

class Role(enum.Enum):
    """Enum representing different CRUD operations."""

    LIST = "list"
    CREATE = "create"
    DETAIL = "detail"
    UPDATE = "update"
    DELETE = "delete"

    def handlers(self) -> dict[str, str]: ...
    def extra_initkwargs(self) -> dict[str, str]: ...
    @property
    def url_name_component(self) -> str: ...
    def url_pattern(self, view_cls: type[CRUDView[_ModelT]]) -> str: ...
    def get_url(self, view_cls: type[CRUDView[_ModelT]]) -> URLPattern: ...
    def reverse(
        self,
        view: CRUDView[_ModelT],
        object: _ModelT | None = None,
    ) -> str: ...
    def maybe_reverse(
        self,
        view: CRUDView[_ModelT],
        object: _ModelT | None = None,
    ) -> str | None: ...

class CRUDView(View, Generic[_ModelT]):
    """Base class for CRUD views providing list, detail, create, update, and delete operations."""

    role: Role
    model: type[_ModelT] | None
    fields: list[str] | None

    lookup_field: str = "pk"
    lookup_url_kwarg: str | None = None
    path_converter: str = "int"
    object: _ModelT | None = None

    queryset: QuerySet[_ModelT] | None
    form_class: type[ModelForm[_ModelT]] | None
    template_name: str | None
    context_object_name: str | None

    paginate_by: int | None = None
    page_kwarg: str = "page"
    allow_empty: bool = True

    template_name_suffix: str | None = None
    object_list: QuerySet[_ModelT] | None = None

    def list(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def detail(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse: ...
    def show_form(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse: ...
    def process_form(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse: ...
    def confirm_delete(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse: ...
    def process_deletion(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponseRedirect: ...
    def get_queryset(self) -> QuerySet[_ModelT]: ...
    def get_object(self) -> _ModelT: ...
    def get_form_class(self) -> type[ModelForm[_ModelT]]: ...
    def get_form(
        self,
        data: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> ModelForm[_ModelT]: ...
    def form_valid(self, form: ModelForm[_ModelT]) -> HttpResponseRedirect: ...
    def form_invalid(self, form: ModelForm[_ModelT]) -> HttpResponse: ...
    def get_success_url(self) -> str: ...
    def get_paginate_by(self) -> int | None: ...
    def get_paginator(
        self,
        queryset: QuerySet[_ModelT],
        page_size: int,
    ) -> Paginator[_ModelT]: ...
    def paginate_queryset(
        self,
        queryset: QuerySet[_ModelT],
        page_size: int,
    ) -> Page[_ModelT]: ...
    def get_filterset(
        self,
        queryset: QuerySet[_ModelT] | None = None,
    ) -> BaseFilterSet | None: ...
    def get_context_object_name(self, is_list: bool = False) -> str | None: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_template_names(self) -> builtins.list[str]: ...
    def render_to_response(self, context: dict[str, Any]) -> TemplateResponse: ...
    @classmethod
    def as_view(  # type: ignore[override]
        cls,
        role: Role,
        **initkwargs: Any,
    ) -> Callable[..., HttpResponseBase]: ...
    url_base: classproperty[str]
    @classmethod
    def get_urls(
        cls,
        roles: builtins.list[Role] | None = None,
    ) -> builtins.list[URLPattern]: ...
