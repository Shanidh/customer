from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Create the Shop User"

    def handle(self, *args, **kwargs):
        try:
            User.objects.create_user(
                username="admin",
                password="admin@123",
                email="admin@gmail.com",
                is_superuser=True,
            )
            self.stdout.write(self.style.SUCCESS("Shop user created successfully."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))