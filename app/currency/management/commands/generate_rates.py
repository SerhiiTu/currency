import random

from django.core.management.base import BaseCommand

from currency.models import Rate, Source
from currency.choices import CurrencyTypeChoices


class Command(BaseCommand):

    help = 'Generate 500 Rate objects' # NOQA A003

    def handle(self, *args, **options):
        source, _ = Source.objects.get_or_create(
            code_name='dummy',
            defaults={
                'name': 'Dummy Source'
            }
        )

        for _ in range(500):
            Rate.objects.create(
                buy=random.randint(30, 40),
                sell=random.randint(30, 40),
                rate_type=random.choice(CurrencyTypeChoices.choices)[0],
                source=source
            )
