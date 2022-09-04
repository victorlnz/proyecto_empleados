from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path("prueba-form",views.PruebaFormCreateView.as_view(),name="crear_form"),
    path("prueba-foundation",views.PruebaFoundation.as_view(),name="prueba-foundation")
]