from django.db.models.signals import pre_save
from django.dispatch import receiver

from account.models import User


@receiver(pre_save, sender=User)
def fix_user_phone(instance, **kwargs):
    phone = instance.phone_number

    for char in phone:
        if not char.isdigit():
            phone = phone.replace(char, '')

    instance.phone_number = phone
