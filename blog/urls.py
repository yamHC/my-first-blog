from django.urls import path
from . import views

# Aca importamos el archivo views.py, que es donde tenemos las vistas de nuestra app blog 

urlpatterns = [
    path('', views.post_list, name='post_list'), # Importamos la vista post_list de views.py y le asignamos la url /
]