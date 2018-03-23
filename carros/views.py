# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Carro
# Create your views here.


def index(request):
    todos_carros = Carro.objects.all()
    template = loader.get_template('carros/index.html')
    return HttpResponse(template.render({'carros': todos_carros}, request))


def detail(request, carro_id):
    carro = Carro.objects.get(id = carro_id)
    return render(request, 'carros/detail.html', {'item': carro})


def fabricante(request):
    todas_marcas = Fabricante.objects.all()
    template = loader.get_template('carros/fabricante.html')
    return HttpResponse(template.render({'fabricante': todas_marcas}, request))
