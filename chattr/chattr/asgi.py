import os

import django.core.asgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chattr.settings')

application = django.core.asgi.get_asgi_application()
