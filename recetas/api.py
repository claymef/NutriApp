# recetas/api.py
from ninja import Router
from typing import List
from .models import Receta, RecetaDetalle
from .schemas import RecetaOutSchema, RecetaInSchema
from django.db import transaction

router = Router()

@router.get("/", response=List[RecetaOutSchema])
def listar_recetas(request):
    return Receta.objects.prefetch_related('ingredientes__alimento').all()

@router.post("/", response=RecetaOutSchema)
def crear_receta(request, payload: RecetaInSchema):
    data = payload.dict()
    ingredientes_data = data.pop('ingredientes')
    
    with transaction.atomic(): # Asegura que si falla un ingrediente, no se guarde la receta a medias
        receta = Receta.objects.create(**data)
        for ing in ingredientes_data:
            RecetaDetalle.objects.create(
                receta=receta,
                alimento_id=ing['alimento_id'],
                cantidad_gramos=ing['cantidad_gramos']
            )
    
    return receta