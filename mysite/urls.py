from django.contrib import admin
from django.urls import path, include

# Aca importamos el modulo include, que nos permite incluir otras urls en nuestro proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # Aca vamosa incluir de include a blog.urls, que es el archivo urls.py de la app blog
]