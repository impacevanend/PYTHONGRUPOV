from django.db import models
from .factura import Factura
from .producto import Producto



class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, related_name='venta', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='venta', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    
    
    
    def __str__(self):
        
        return f'Venta {self.id}: {self.factura} {self.producto} {self.cantidad}'
    