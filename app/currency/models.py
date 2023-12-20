from django.db import models

from currency.choices import CurrencyTypeChoices


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    rate_type = models.SmallIntegerField(
        choices=CurrencyTypeChoices.choices,
    )
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rate_type} - {self.buy} - {self.sell} - {self.source}"


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    source_type = models.CharField(max_length=50)  # bank, exchanger, etc...

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=8)
    time = models.DecimalField(max_digits=16, decimal_places=3)
