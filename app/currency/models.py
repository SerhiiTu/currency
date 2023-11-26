from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    rate_type = models.CharField(max_length=4)
    source = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    source_type = models.CharField(max_length=50)  # bank, exchanger, etc...
