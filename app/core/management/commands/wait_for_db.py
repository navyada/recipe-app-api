"""
DJANGO command to wait for the database to be available 
"""

from django.core.management.base import BaseCommand

import time 

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django command to wait for the database to be available"""
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database to be available")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable, waiting one second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))