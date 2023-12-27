import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"avatars/user_{instance.id}/{filename}"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.SmallIntegerField()
    created = models.DateTimeField(auto_now=True)
    avatar = models.FileField(default=None, null=True, blank=True, upload_to=user_directory_path)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = uuid.uuid4()

        return super().save(*args, **kwargs)
