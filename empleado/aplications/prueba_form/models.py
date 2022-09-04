from django.db import models

# Create your models here.

class PruebaForm(models.Model):

    titulo = models.CharField("Titulo", max_length=50)
    subtitulo = models.CharField("Abreviacion", max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + "-" + self.subtitulo

        