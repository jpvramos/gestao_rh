from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from apps.funcionarios.models import Funcionario


def funcionarios(request):
    return HttpResponse('Ola')


class FuncionariosList():
    model = Funcionario
