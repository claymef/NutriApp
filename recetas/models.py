from django.db import models
import uuid
from catalogo.models import Alimento

class Receta(models.Model):
    id_receta = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class RecetaDetalle(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='ingredientes')
    alimento = models.ForeignKey(Alimento, on_delete=models.RESTRICT)
    cantidad_gramos = models.DecimalField(max_digits=7, decimal_places=2)

    # Aquí implementamos la regla de tres simple para el cálculo nutricional
    @property
    def proteinas_aportadas(self):
        return (self.cantidad_gramos * self.alimento.proteinas_g) / 100
    
    @property
    def energia_aportada(self):
        return (self.cantidad_gramos * self.alimento.energia_kcal) / 100