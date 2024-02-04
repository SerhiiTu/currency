from unittest.mock import MagicMock

from currency.choices import CurrencyTypeChoices
from currency.constants import PRIVATBANK_CODE_NAME
from currency.models import Rate, Source
from currency.tasks import parse_privatbank, parse_monobank


def test_parse_privatbank(mocker):
    initial_count = Rate.objects.count()

    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "40.80000", "sale": "41.80000"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data)
    )

    parse_privatbank()

    assert Rate.objects.count() == initial_count + 2
    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args[0][0] == 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'


def test_parse_privatbank_prevent_duplicates(mocker):
    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "40.80000", "sale": "41.80000"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data)
    )
    source = Source.objects.get(code_name=PRIVATBANK_CODE_NAME)
    Rate.objects.create(source=source, buy="40.80", sell="41.80", rate_type=CurrencyTypeChoices.EUR)
    Rate.objects.create(source=source, buy="37.50", sell="38.10", rate_type=CurrencyTypeChoices.USD)
    initial_count = Rate.objects.count()

    parse_privatbank()

    assert Rate.objects.count() == initial_count
    assert requests_get_mock.call_count == 1


def test_parse_monobank(mocker):
    initial_count = Rate.objects.count()

    monobank_data = [
        {"currencyCodeA": 840, "currencyCodeB": 980, "date": 1706997673, "rateBuy": 37.47, "rateSell": 38.0098},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1706997673, "rateBuy": 40.45, "rateSell": 41.2201},
        {"currencyCodeA": 978, "currencyCodeB": 840, "date": 1706997673, "rateBuy": 1.075, "rateSell": 1.09},
        {"currencyCodeA": 826, "currencyCodeB": 980, "date": 1707082663, "rateCross": 48.5696},
        {"currencyCodeA": 392, "currencyCodeB": 980, "date": 1707082164, "rateCross": 0.2602},
        {"currencyCodeA": 756, "currencyCodeB": 980, "date": 1707082609, "rateCross": 44.4573},
        {"currencyCodeA": 156, "currencyCodeB": 980, "date": 1707081483, "rateCross": 5.2822},
        {"currencyCodeA": 784, "currencyCodeB": 980, "date": 1707082654, "rateCross": 10.3545},
        {"currencyCodeA": 971, "currencyCodeB": 980, "date": 1703852583, "rateCross": 0.5417},
        {"currencyCodeA": 8, "currencyCodeB": 980, "date": 1707082507, "rateCross": 0.3961},
        {"currencyCodeA": 51, "currencyCodeB": 980, "date": 1707080151, "rateCross": 0.0947}
    ]

    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: monobank_data)
    )

    parse_monobank()

    assert Rate.objects.count() == initial_count + 2
    assert requests_get_mock.call_count == 1


def test_parse_monobank_prevent_duplicates(mocker):
    monobank_data = [
        {"currencyCodeA": 840, "currencyCodeB": 980, "date": 1706997673, "rateBuy": 37.47, "rateSell": 38.00},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1706997673, "rateBuy": 40.45, "rateSell": 41.22},
        {"currencyCodeA": 978, "currencyCodeB": 840, "date": 1706997673, "rateBuy": 1.075, "rateSell": 1.09},
        {"currencyCodeA": 826, "currencyCodeB": 980, "date": 1707082663, "rateCross": 48.5696},
        {"currencyCodeA": 392, "currencyCodeB": 980, "date": 1707082164, "rateCross": 0.2602},
        {"currencyCodeA": 756, "currencyCodeB": 980, "date": 1707082609, "rateCross": 44.4573},
        {"currencyCodeA": 156, "currencyCodeB": 980, "date": 1707081483, "rateCross": 5.2822},
        {"currencyCodeA": 784, "currencyCodeB": 980, "date": 1707082654, "rateCross": 10.3545},
        {"currencyCodeA": 971, "currencyCodeB": 980, "date": 1703852583, "rateCross": 0.5417},
        {"currencyCodeA": 8, "currencyCodeB": 980, "date": 1707082507, "rateCross": 0.3961},
        {"currencyCodeA": 51, "currencyCodeB": 980, "date": 1707080151, "rateCross": 0.0947}
    ]

    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: monobank_data)
    )

    parse_monobank()

    initial_count = Rate.objects.count()

    parse_monobank()

    assert Rate.objects.count() == initial_count
    assert requests_get_mock.call_count == 2
