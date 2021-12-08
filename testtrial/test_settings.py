from .settings import *             # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':db:'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'