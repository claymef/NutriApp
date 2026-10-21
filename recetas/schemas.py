# recetas/schemas.py
from ninja import ModelSchema
from typing import List
from .models import Receta, RecetaDetalle

class IngredienteOutSchema(ModelSchema):
    nombre_alimento: str
    proteinas_aportadas: float
    energia_aportada: float

    class Meta:
        model = RecetaDetalle
        fields = ['cantidad_gramos']

    # Resolvemos el nombre del alimento desde la relación ForeignKey
    @staticmethod
    def resolve_nombre_alimento(obj):
        return obj.alimento.nombre

class RecetaOutSchema(ModelSchema):
    ingredientes: List[IngredienteOutSchema]

    class Meta:
        model = Receta
        fields = ['id_receta', 'nombre', 'categoria']

class IngredienteInSchema(ModelSchema):
    alimento_id: str # Recibiremos el UUID del alimento

    class Meta:
        model = RecetaDetalle
        fields = ['cantidad_gramos']

class RecetaInSchema(ModelSchema):
    ingredientes: List[IngredienteInSchema]

    class Meta:
        model = Receta
        fields = ['nombre', 'categoria']