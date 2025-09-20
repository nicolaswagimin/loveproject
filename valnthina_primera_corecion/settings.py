import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ["*", "localhost", "127.0.0.1"]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Para producción, usa una clave secreta desde variables de entorno
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "clave-insegura-para-dev")

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',  # Para desarrollo local
        conn_max_age=600
    )
}