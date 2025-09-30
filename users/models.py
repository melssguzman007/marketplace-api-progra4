# users/models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    # NOTA: En un proyecto real, nunca guardarías la contraseña así.
    # Usarías el sistema de usuarios de Django o hashers.
    password = models.CharField(max_length=128) 

    def __str__(self):
        return self.username