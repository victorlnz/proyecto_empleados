from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .models import *
from .forms import PruebaFormform
# Create your views here.

class PruebaFoundation(TemplateView):
    template_name = "prueba_form/prueba-foundation.html"


class PruebaFormCreateView(CreateView):
    template_name = "prueba_form/add.html"
    model = PruebaForm
    form_class = PruebaFormform
    success_url = "/"

