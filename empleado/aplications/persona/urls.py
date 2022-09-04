from django.urls import path
from . import views
from django.contrib import admin

app_name = "persona_app" 

urlpatterns = [
    path(
        "",
        views.InicioView.as_view(),
        name="inicio"
    ),
    path(
        "listar-empleados",
        views.MostrarEmpleados.as_view(),
        name="listar-all"        
    ),
    path("listar-por-departamento/<shorname>",
        views.listar_por_area.as_view(),
        name="empleado-departamento"
    ),
    path("list_all_admin",
        views.MostrarEmpleadosAdmin.as_view(),
        name="list_admin"
    ),
    path("listar-por-trabajo/<laburo>",views.listar_por_trabajo.as_view()),
    path("listar_por_kword/",views.listar_empleado_por_keyword.as_view()),
    path("listar_habilidad/",views.Habilidades_de_Empleados.as_view()),
    path(
        "detalle-vista/<pk>",
        views.EmpleadoDetailView.as_view(),
        name="detalle-empleado"
    ),
    path("agregar-empleado",
    views.EmpleadoCreateView.as_view(),
    name="add-empleado"
    ),
    path("success",views.Successview.as_view(),name="correcto"),
    path("update-empleado/<pk>",
        views.EmpleadoUpdateView.as_view(),
        name="modificar_empleado"
    ),
    path("delete-empleado/<pk>",
    views.EmpleadoDeleteView.as_view(),
    name="borrar-empleado")

]