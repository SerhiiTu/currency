from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    rate_type = models.CharField(max_length=4)
    source = models.CharField(max_length=255)
    created = models.DateTimeField()


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()
