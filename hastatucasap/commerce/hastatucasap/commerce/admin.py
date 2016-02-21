from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Precio)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Clasificacion)
admin.site.register(Empresa)
admin.site.register(Producto_precio)
admin.site.register(Pedido)