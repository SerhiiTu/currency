from settings.settings import * # NOQA

DEBUG = False

CELERY_TASK_ALWAYS_EAGER = True

CACHES = {
    "default.conf": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}
