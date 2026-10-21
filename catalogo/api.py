# catalogo/api.py
from ninja import Router
from typing import List
from .models import Alimento
from .schemas import AlimentoInSchema, AlimentoSchema, AlimentoInSchema

router = Router()

@router.get("/alimentos", response=List[AlimentoSchema])
def listar_alimentos(request):
    return Alimento.objects.all().order_by('nombre')

@router.post("/alimentos", response=AlimentoSchema)
def crear_alimento(request, payload: AlimentoInSchema):
    alimento = Alimento.objects.create(**payload.dict())
    return alimento