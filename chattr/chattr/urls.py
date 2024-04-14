from django.contrib import admin
from django.urls import include
from django.urls import path
import homepage.urls

import api.urls

urlpatterns = [
    path(
        '',
        include(homepage.urls),
    ),
    path(
        'api/',
        include(api.urls),
    ),
    path('admin/', admin.site.urls),
]
