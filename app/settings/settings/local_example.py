from .base import * # NOQA 403

DEBUG = True

DATABASES = {
    'default.conf': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', # NOQA 405
    }
}
