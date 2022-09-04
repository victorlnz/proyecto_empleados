from django.shortcuts import render
from .forms import NewDepartamentoForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from aplications.persona.models import Empleado
from .models import Departamento
# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/listview_depa.html"
    context_object_name = "depas"


class NewDepartamentoView(FormView):
    template_name = "departamento/new_departamento.html"
    form_class = NewDepartamentoForm
    success_url = "/"

    def form_valid(self, form):

        depa = Departamento(
            name = form.cleaned_data["departamento"],
            short_name = form.cleaned_data["shorname"]
        )
        depa.save()

        #recuperar los datos del formulario
        nombre = form.cleaned_data["nombre"]
        apellido = form.cleaned_data["apellido"]
        #hacer registro en el modelo empleado
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = "1",
            departamento = depa,
            hoja_vida = "creado por la funcion new"
        )
        
        return super(NewDepartamentoView,self).form_valid(form) 






