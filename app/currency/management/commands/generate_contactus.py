import random
import names

from django.core.management.base import BaseCommand

from currency.models import ContactUs


class Command(BaseCommand):

    def handle(self, *args, **options):
        for _ in range(500):
            ContactUs.objects.create(
                name=f"{names.get_first_name()}",
                email_from=f"{names.get_last_name()}@gmail.com",
                subject=f"TestSubject{random.randint(1, 1000)}",
                message=f"{random.randint(10000, 100000)}"
            )
