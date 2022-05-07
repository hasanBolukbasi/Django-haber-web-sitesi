from django.urls import path, include
from django.contrib import admin

from .import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('news', include('news.urls')),
    path('home', include('home.urls')),
    path('', include('home.urls')),
]
