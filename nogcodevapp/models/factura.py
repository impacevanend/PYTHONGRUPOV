from django.db import models
from .usuario import User
class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='factura', on_delete=models.CASCADE)
    fecha = models.DateField()
    
    
    
    def __str__(self):
        
        return f'Factura {self.id}: {self.user} {self.fecha}'
