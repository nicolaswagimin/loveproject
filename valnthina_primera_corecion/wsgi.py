import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'valnthina_primera_corecion.settings')

application = get_wsgi_application()