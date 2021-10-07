from django.db import models
from .usuario import User


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, related_name='factura', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=0)
    