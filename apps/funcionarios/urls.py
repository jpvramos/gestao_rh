from django.urls import path, include

from apps.funcionarios import views


urlpatterns = [
    path('', views.funcionarios, name='funcionarios'),
    path('funcionarios/', views.FuncionariosList, name='funcionarios_list'),
]