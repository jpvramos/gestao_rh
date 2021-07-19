from django.urls import path
from apps.empresas import views


urlpatterns = [
  path('novo/', views.EmpresaCreateView.as_view(), name="empresa_create"),
  path('editar/<int:pk>', 
        views.EmpresaEditView.as_view(), 
        name="empresa_edit"),
]