from django.contrib import admin
from .models import Receta, RecetaDetalle

class RecetaDetalleInline(admin.TabularInline):
    model = RecetaDetalle
    extra = 3  # Filas en blanco por defecto para agregar ingredientes
    autocomplete_fields = ['alimento'] # Activa un buscador de alimentos en lugar de un menú desplegable simple

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre',)
    inlines = [RecetaDetalleInline]