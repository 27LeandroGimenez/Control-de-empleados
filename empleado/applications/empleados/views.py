from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empleado

# Create your views here.

class InicioView(TemplateView):
    # vista que carga la pagina de inicio
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 5
    ordering = 'first_name'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(first_name__icontains=palabra_clave)
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'empleados/lista_empleados.html'
    paginate_by = 5
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

class ListByArea(ListView):
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(departamento__shor_name=area)
        return lista

class ListByTrabajo(ListView):
    template_name = 'empleados/list_by_trabajo.html'

    def get_queryset(self):
        trabajo = self.kwargs['trabajo']
        lista = Empleado.objects.filter(job=trabajo)
        return lista

class ListEmpleadosByKword(ListView):
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        return lista

class ListHabilidadesEmpleados(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()

# Details views 
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = ''
        return context


class SuccessView(TemplateView):
    template_name = "empleados/success.html"


#Create view
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleados/add.html'
    fields = ['first_name', 'last_name', 'departamento', 'job', 'habilidades', 'avatar',]
    success_url = reverse_lazy('empleados_app:empleados_admin')

    #concatenar datos 
    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

#Update views

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleados/update.html"
    fields = ['first_name', 'last_name', 'departamento', 'job', 'habilidades']
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

#Delete views

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('empleados_app:empleados_admin')

