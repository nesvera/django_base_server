""""
Django command to wait for the database to be available.
"""
import time
from typing import Any, Optional

from psycopg import OperationalError as PsycopgError

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """" Django command to wait for database. """

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        """Entrypoint for command."""
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True

            except (PsycopgError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is ready!"))
