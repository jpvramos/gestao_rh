from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView

from apps.empresas.models import Empresa


class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ['nome', ]
    
    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('ok')

class EmpresaEditView(UpdateView):
    model = Empresa
    fields = ['nome',]