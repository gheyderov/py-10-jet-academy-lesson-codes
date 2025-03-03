from django.core.management.base import BaseCommand
from faker import Faker
fake = Faker()
from django.contrib.auth import get_user_model
User = get_user_model()


class Command(BaseCommand):
    help = "Used to create fake users."
    requires_migrations_checks = True
    stealth_options = ("stdin",)

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int)
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        for i in range(options['number']):
            User.objects.create(
                username = fake.name(),
                email = fake.email(),
                is_active = False
            )