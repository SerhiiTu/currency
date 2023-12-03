from django.db import models


class CurrencyTypeChoices(models.IntegerChoices):
    USD = 1, "USD"
    EUR = 2, "EUR"
    DBP = 3, "GBP"
    PLN = 4, "PLN"
    CAD = 5, "CAD"
