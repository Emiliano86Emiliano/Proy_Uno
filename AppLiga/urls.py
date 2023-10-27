from django.contrib import admin
from django.urls import path
from AppLiga.views import equipo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipo/', equipo)
]

