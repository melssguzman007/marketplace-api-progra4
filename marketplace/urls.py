# marketplace/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ⬇️ Rutas de la API de Usuarios ⬇️
    path('api/', include('users.urls')),
    # ⬆️ Rutas de la API de Usuarios ⬆️
]
