from django.contrib import admin
from .models import Alimento

@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'energia_kcal', 'proteinas_g', 'carbohidratos_g', 'grasas_g', 'precio_unitario')
    search_fields = ('nombre',) # Esencial para el buscador
    ordering = ('nombre',)