from django.db import models

from aplications.departamento.models import Departamento

from ckeditor.fields import RichTextField
# Create your models here.

class Habilidad(models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)

    class Meta:
        verbose_name = "Habilidade"
        

    def __str__(self):
        return self.habilidad     



class Empleado(models.Model):
    """ Modelo para tabla empleado"""

    tipo_job = (
        ("0","Contador"),
        ("1","Administrador"),
        ("2","Economista"),
        ("3","Otros"),

    )

    first_name = models.CharField("Nombres", max_length=50)
    last_name = models.CharField("Apellidos", max_length=50)
    job = models.CharField("Trabajo", max_length=1,choices=tipo_job)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    full_name = models.CharField("Full name",max_length=120,blank=True)
    imagen = models.ImageField("Foto", upload_to="empleado", blank=True,null=True)
    habilidades = models.ManyToManyField(Habilidad,blank=True)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = "Empleados de la empresa"
        ordering = ["first_name"]
        unique_together = ("first_name","last_name","job")


    def __str__(self):
        return str(self.id) + "-" + self.first_name + "-" + self.last_name
        