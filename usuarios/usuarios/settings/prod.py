from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = 'static/'
STATICFILES_DIRS = ['static/']


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'