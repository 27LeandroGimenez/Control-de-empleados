from django.contrib import admin
from django.urls import path
from . import views

app_name = 'empleados_app'

urlpatterns=[
    path('', views.InicioView.as_view(), name='inicio'), 
    path('listar-todo-empleado/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('listar-by-area/<shorname>/', views.ListByArea.as_view(), name='empleados_area'),
    path('lista-empleados-admin', views.ListaEmpleadosAdmin.as_view(), name='empleados_admin'),
    path('listar-by-trabajo/<trabajo>/', views.ListByTrabajo.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('habilidades-empleado/', views.ListHabilidadesEmpleados.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detalle'),
    path('crear-empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]