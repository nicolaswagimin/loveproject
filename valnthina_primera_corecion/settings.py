import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "clave-insegura-para-dev")
DEBUG = False
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    # ...tus apps...
    'django.contrib.staticfiles',
    # ...tus apps...
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}