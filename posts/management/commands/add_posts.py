from typing import Any, Optional
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Hello")
        self.stdout.write("hello")
        