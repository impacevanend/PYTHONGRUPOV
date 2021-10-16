from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.core import serializers

from nogcodevapp.models import Producto

def listadoProducto(request):
    lista = serializers.serialize('json', Producto.objects.all())
    return HttpResponse(lista, content_type='application/json')