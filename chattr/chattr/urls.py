from django.contrib import admin
from django.urls import include
from django.urls import path
import django.views.generic

import api.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        django.views.generic.TemplateView.as_view(template_name='index.html'),
    ),
    path(
        'api/',
        include(api.urls),
    ),
]
