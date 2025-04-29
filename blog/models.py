from django.conf import settings
from django.db import models
from django.utils import timezone

# Aca creamos todos los modelos(tablas) de la BD

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # Aca creamos un metodo que se llama publish, que lo que hace es guardar la fecha de publicacion
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Aca creamos un metodo que se llama __str__, que lo que hace es devolver el titulo del post
    def __str__(self):
        return self.title