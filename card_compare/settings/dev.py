from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'card_compare',
        'USER': 'postgres',
        'PASSWORD': 'psql',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}   