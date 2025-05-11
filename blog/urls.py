from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Ruta para la lista de posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Ruta para el detalle de un post
]