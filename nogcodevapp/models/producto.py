from django.db import models
from .categoria import Categoria



class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, related_name='producto', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.CharField(max_length=255)
    
    
    def __str__(self):
        
        return f'Producto {self.id}: {self.categoria} {self.precio}'
    