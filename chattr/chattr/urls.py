from django.contrib import admin
from django.urls import include
from django.urls import path

import api.urls
import chat.urls
import homepage.urls

urlpatterns = [
    path(
        '',
        include(homepage.urls),
    ),
    path(
        'api/',
        include(api.urls),
    ),
    path(
        'admin/',
        admin.site.urls,
    ),
    path(
        'chat/',
        include(chat.urls),
    ),
]
