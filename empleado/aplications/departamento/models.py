from django.db import models

# Create your models here.

class Departamento(models.Model):

    name = models.CharField("Nombre",max_length=30,)
    short_name = models.CharField("Nombre abreviado",max_length=20)
    anulate = models.BooleanField("Anulado",default=False)

    class Meta:
        verbose_name = "Controlador de Departamento"
        ordering = ["id"]    

    def __str__(self):
        return str(self.id) + "-" + self.name + "-" + self.short_name 

