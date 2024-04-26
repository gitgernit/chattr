__all__ = []

import os
import pathlib

import dotenv

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

dotenv.load_dotenv()

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', default='NOTSET')

true_values = ('true', 't', 'y', '1')
DEBUG = os.getenv('DJANGO_DEBUG', default='False').lower() in true_values

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', default='*').split()

INTERNAL_IPS = os.getenv('DJANGO_ALLOWED_HOSTS', default='').split()

DB_HOST = os.getenv('POSTGRES_HOST', default='localhost')
DB_PORT = os.getenv('POSTGRES_PORT', default=5432)
DB_NAME = os.getenv('POSTGRES_NAME', default='postgres')
DB_USER = os.getenv('POSTGRES_USER', default='testuser')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', default='testpassword')

REDIS_HOST = os.getenv('REDIS_HOST', default='127.0.0.1')
REDIS_PORT = os.getenv('REDIS_PORT', default='6379')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'rest_framework',
] + [
    'api.homepage.apps.ApiHomepageConfig',
    'homepage.apps.HomepageConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chattr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'chattr-react/dist/'],
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

WSGI_APPLICATION = 'chattr.wsgi.application'
ASGI_APPLICATION = 'chattr.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}'],
            'symmetric_encryption_keys': [SECRET_KEY],
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': REDIS_PASSWORD,
        },
    },
}

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS = {
    'host': REDIS_HOST,
    'port': REDIS_PORT,
    'password': REDIS_PASSWORD,
    'db': 1,
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.NumericPasswordValidator'
        ),
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'static/'

STATICFILES_DIRS = [BASE_DIR / 'chattr-react/dist/static/']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
