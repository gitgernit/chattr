from django.contrib import admin
from django.urls import path
import django.views.generic

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        django.views.generic.TemplateView.as_view(template_name='index.html'),
    ),
]
