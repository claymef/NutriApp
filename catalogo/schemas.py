# catalogo/schemas.py
from ninja import ModelSchema
from .models import Alimento

class AlimentoSchema(ModelSchema):
    class Meta:
        model = Alimento
        fields = "__all__"

class AlimentoInSchema(ModelSchema):
    class Meta:
        model = Alimento
        exclude = ["id_alimento"]