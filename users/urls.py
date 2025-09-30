# users/urls.py

from django.urls import path # Necesitas importar path
from .views import user_form # Necesitas importar la función
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

# Agrega la ruta del formulario a las rutas del router
urlpatterns = router.urls + [
    path("form/", user_form, name="user_form"),
]