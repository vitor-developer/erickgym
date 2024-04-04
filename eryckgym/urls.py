from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('treinos.urls')),
    path('', include('cadastro.urls')),
    path("admin/", admin.site.urls),
]