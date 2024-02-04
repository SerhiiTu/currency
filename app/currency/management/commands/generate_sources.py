import random
import names

from django.core.management.base import BaseCommand

from currency.models import Source


class Command(BaseCommand):

    help = 'Generate 500 Source objects' # NOQA A003

    def handle(self, *args, **options):
        for _ in range(500):
            Source.objects.create(
                source_url=f'http://testsource{random.randint(1, 1000)}.com',
                name=f"{names.get_first_name()}`s Bank",
                source_type=f"{random.choice(['bank', 'exchanger', 'other'])}",
                code_name=f'{random.randint(1, 100000)}-{random.randint(1, 100000)}-{random.randint(1, 100000)}',
            )
