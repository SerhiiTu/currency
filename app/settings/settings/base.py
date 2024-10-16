import environ
from pathlib import Path

from datetime import timedelta
from celery.schedules import crontab
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!

env = environ.Env(
    DEBUG=(bool, False)
)
env.read_env(BASE_DIR.parent / '.env')

SECRET_KEY = env.str('SECRET_KEY')

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'django_filters',
    'crispy_forms',
    'crispy_bootstrap4',
    'rest_framework',

    'currency',
    'account',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB', 'currency-db'),
        'USER': env.str('POSTGRES_USER', 'currency'),
        'PASSWORD': env.str('POSTGRES_PASSWORD', ''),
        'HOST': env.str('POSTGRES_HOST', 'localhost'),
        'PORT': env.str('POSTGRES_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'account.User'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # 401
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # 403
    ),
    'DEFAULT_THROTTLE_RATES': {
        'rate': '10/min'
    },
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=14),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer', 'JWT',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# STATIC_ROOT = BASE_DIR / 'var/static'
STATIC_ROOT = '/tmp/static'

MEDIA_URL = 'var/'
MEDIA_ROOT = BASE_DIR / 'var/var'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'hileltest1234@gmail.com'

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('login')
LOGOUT_REDIRECT_URL = reverse_lazy('index')

HTTP_METHOD = 'http'
DOMAIN = '0.0.0.0:8000'

RABBITMQ_USER = env.str('RABBITMQ_DEFAULT_USER', 'guest')
RABBITMQ_PASS = env.str('RABBITMQ_DEFAULT_PASS', 'guest')
RABBITMQ_HOST = env.str('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = env.str('RABBITMQ_PORT', '5672')

CELERY_BROKER_URL = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}:{RABBITMQ_PORT}'
# amqp, localhost, port=5672, user=guest, password=guest

# MEMCACHED_HOST = env.str('MEMCACHED_HOST', 'localhost')
# MEMCACHED_PORT = env.str('MEMCACHED_PORT', '11211')
# CACHES = {
#     "default.conf": {
#         "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
#         "LOCATION": f"{MEMCACHED_HOST}:{MEMCACHED_PORT}",
#     }
# }

CELERY_BEAT_SCHEDULE = {
    'parse_privatbank': {
        'task': 'currency.tasks.parse_privatbank',
        'schedule': crontab(minute='*/1')
    },

    'parse_monobank': {
        'task': 'currency.tasks.parse_monobank',
        'schedule': crontab(minute='*/1')
    }

}
