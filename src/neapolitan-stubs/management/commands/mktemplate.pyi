"""Type stubs for Neapolitan management commands. https://github.com/nkantar/neapolitan-stubs"""

from typing import Any
from argparse import ArgumentParser
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help: str

    def add_arguments(self, parser: ArgumentParser) -> None: ...
    def handle(self, *args: Any, **options: Any) -> None: ...
