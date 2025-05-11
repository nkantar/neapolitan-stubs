"""Type stubs for Neapolitan. https://github.com/nkantar/neapolitan-stubs"""

from typing import Any

from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "Bootstrap a CRUD template for a model, copying from the active neapolitan default templates."

    def add_arguments(self, parser: CommandParser) -> None: ...

    def handle(self, *args: Any, **options: Any) -> None: ...
