from django.db import models

from currency.choices import CurrencyTypeChoices


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"logos/sources/source_{instance.id}/{filename}"


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
    code_name = models.CharField(max_length=64, unique=True)
    source_type = models.CharField(max_length=50)  # bank, exchanger, etc...
    logo = models.FileField(default=None, null=True, blank=True, upload_to=user_directory_path)

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=8)
    time = models.DecimalField(max_digits=16, decimal_places=3)
