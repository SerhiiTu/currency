from decimal import Decimal, ROUND_DOWN
from celery import shared_task
from django.conf import settings
import requests

from currency.constants import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME, HRYVNIA_CODE
from currency.models import Rate, Source
from currency.choices import CurrencyTypeChoices
from currency.utils import to_2_places_decimal
from decimal import Decimal, ROUND_DOWN
from django.core.mail import send_mail


@shared_task
def send_mail_in_background(subject, body):
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )


@shared_task
def parse_privatbank():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    response = requests.get(url)
    response.raise_for_status()

    source, _ = Source.objects.get_or_create(code_name=MONOBANK_CODE_NAME, defaults={'name': 'MonoBank'})

    rates = response.json()

    available_currency_types = {
        'USD': CurrencyTypeChoices.USD,
        'EUR': CurrencyTypeChoices.EUR
    }

    for rate in rates:
        buy = to_2_places_decimal(rate['buy'])
        sell = to_2_places_decimal(rate['sale'])
        rate_type = rate['ccy']

        if rate_type not in available_currency_types:
            continue

        rate_type = available_currency_types[rate_type]

        last_rate = Rate.objects.filter(source=source, rate_type=rate_type).order_by('-created').first()

        if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
            Rate.objects.create(
                buy=buy,
                sell=sell,
                rate_type=rate_type,
                source=source
            )


@shared_task
def parse_monobank():
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()

    source, _ = Source.objects.get_or_create(code_name=MONOBANK_CODE_NAME, defaults={'name': 'Monobank'})

    rates = response.json()

    available_currency_types = {
        840: CurrencyTypeChoices.USD,
        978: CurrencyTypeChoices.EUR
    }

    for rate in rates:
        rate_type = rate['currencyCodeA']
        rate_pair_type = rate['currencyCodeB']
        if rate_type not in available_currency_types or rate_pair_type != HRYVNIA_CODE:
            continue

        buy = to_2_places_decimal(rate['rateBuy'])
        sell = to_2_places_decimal(rate['rateSell'])

        rate_type = available_currency_types[rate_type]

        last_rate = Rate.objects.filter(source=source, rate_type=rate_type).order_by('-created').first()

        if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
            Rate.objects.create(
                buy=buy,
                sell=sell,
                rate_type=rate_type,
                source=source
            )
