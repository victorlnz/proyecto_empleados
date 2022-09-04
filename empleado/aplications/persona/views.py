from django.shortcuts import render

from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
from .models import Empleado
from django.urls import reverse_lazy

#forms
from .forms import EmpleadoForm

# Create your views here.

class InicioView(TemplateView):
    #vista que carga la pagina de inicio
    template_name = "inicio.html"

class MostrarEmpleados(ListView):
    template_name = "persona/list_all.html"
    #model = Empleado          "cuando añadimos la funcion get_queryset no se utiliza el modelo"
    context_object_name = "list_emple"
    paginate_by = 4

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword","")
        lista= Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )       

        return lista 


class MostrarEmpleadosAdmin(ListView):
    template_name = "persona/list_all_admin.html"
    model = Empleado
    context_object_name = "list_admin"
    ordering = "first_name"
    paginate_by = 10



# vistas de practica
class listar_por_area(ListView):
    template_name = "persona/list_by_departamento.html"
    context_object_name = "empleados"
    

    def get_queryset(self):
        area = self.kwargs["shorname"]
        lista= Empleado.objects.filter(
        departamento__short_name = area)

        return lista

class listar_por_trabajo(ListView):
    template_name = "persona/list_por_trabajo.html"
    context_object_name = "list"
    def get_queryset(self):
        
        trabajo = self.kwargs["laburo"]
        liste= Empleado.objects.filter(
            job = trabajo
        )
        
        return liste

class listar_empleado_por_keyword(ListView):
    template_name = "persona/por_kword.html"
    context_object_name = "array_kword"

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword","")
        lista= Empleado.objects.filter(
            first_name = palabra_clave
        )       

        return lista             

class Habilidades_de_Empleados(ListView):
    template_name = "persona/habilidades.html"
    context_object_name = "hability"

    def get_queryset(self):
        empleado = Empleado.objects.get(id=5)
        
        return empleado.habilidades.all()        


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detailview.html"

    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = "Soy la mera verga"
        return context



class Successview(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/agregar.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:list_admin')

    def form_valid(self, form):
        empleado = form.save()
        concatenar = empleado.first_name + " " + empleado.last_name
        empleado.full_name = concatenar
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = (
        "first_name",
        "last_name",
        "job",
        "departamento",
        "habilidades",
    )

    success_url = reverse_lazy('persona_app:list_admin')   

    def post(self, request, *args, **kwargs):
        #en el metodo post recupera datos enviados al servidor, y funciona en forma de diccionario de python
        dato_a_recuperar = request.POST["last_name"]
        print(dato_a_recuperar)

        return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "Persona/deleteview.html"
    success_url = reverse_lazy('persona_app:list_admin')

    def delete(self, request, *args, **kwargs):
        recuperar = request.POST["first_name","last_name"]
                                        
        return super(EmpleadoDeleteView).delete(request, *args, **kwargs)