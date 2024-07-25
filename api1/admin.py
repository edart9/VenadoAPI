from django.contrib import admin
from .models import cliente, pedido, producto
# Register your models here.

admin.site.register(cliente)
admin.site.register(pedido)
admin.site.register(producto)