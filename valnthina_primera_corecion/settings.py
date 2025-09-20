import os

ALLOWED_HOSTS = ["*", "localhost", "127.0.0.1"]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Para producción, usa una clave secreta desde variables de entorno
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "clave-insegura-para-dev")