from datetime import datetime
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Display all users'

    def handle(self, *args, **options):
        users = get_user_model().objects.all()
        for user in users:
            self.stdout.write(f'Username: {user.email}')