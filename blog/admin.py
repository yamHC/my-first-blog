from django.contrib import admin
from .models import Post  # llamamos al modelo Post que creamos en models.py

# Aca registramos el modelo Post en el admin de Django, para que podamos verlo en la interfaz de admin
admin.site.register(Post)