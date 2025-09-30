# users/views.py

from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from .forms import UserForm # Necesitas importar el formulario

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
def user_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige al endpoint JSON de la API para ver el resultado
            return redirect("/api/users/") 
    else:
        form = UserForm()
    return render(request, "user_form.html", {"form": form})