from django.contrib import admin

from .models import Empleado,Habilidad
# Register your models here.

admin.site.register(Habilidad)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "departamento",
        "job",
        "id",
    )

    list_filter = ("departamento","job","habilidades",)

admin.site.register(Empleado,EmpleadoAdmin)
