# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Fabricante(models.Model):
    nome = models.CharField(max_length = 300)
    def __str__(self):
        return self.nome

class Carro(models.Model):
    name = models.CharField(max_length = 300)
    valor = models.DecimalField(null=True, decimal_places =2, max_digits = 300)
    ano = models.IntegerField(null=True)
    modelo = models.CharField(null=True, max_length = 300)
    fabricante = models.ForeignKey(Fabricante, null=True)
    def __str__(self):
        return self.name






