from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path("new-departamento",
    views.NewDepartamentoView.as_view(),
    name="nuevo-depa"
    ),
    path("lista-by-departamento",
    views.DepartamentoListView.as_view(),
    name="lista-por-depa"
    ),
]