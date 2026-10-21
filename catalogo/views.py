from django.shortcuts import render
from .models import Alimento

def lista_alimentos(request):
    alimentos = Alimento.objects.all().order_by('nombre')
    return render(request, 'catalogo/lista_alimentos.html', {'alimentos': alimentos})