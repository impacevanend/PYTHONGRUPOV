from django.contrib import admin
from .models.usuario import User
from .models.factura import Factura
from .models.venta import Venta
from .models.producto import Producto
from .models.categoria import Categoria




# Register your models here.

admin.site.register(User)
admin.site.register(Factura)
admin.site.register(Venta)
admin.site.register(Producto)
admin.site.register(Categoria)


