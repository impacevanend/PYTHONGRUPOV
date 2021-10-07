from django.db import models
from .factura import Factura


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, related_name='venta', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    