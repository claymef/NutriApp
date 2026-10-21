from django.db import models
import uuid

class Alimento(models.Model):
    id_alimento = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200, unique=True)
    energia_kcal = models.DecimalField(max_digits=7, decimal_places=2)
    proteinas_g = models.DecimalField(max_digits=7, decimal_places=2)
    carbohidratos_g = models.DecimalField(max_digits=7, decimal_places=2)
    grasas_g = models.DecimalField(max_digits=7, decimal_places=2)
    hierro_mg = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    calcio_mg = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre