from django.contrib import admin
from inventario.models import Producto, UnidadMedida, Entrada


class UnidadMedidaAdmin(admin.ModelAdmin):
    pass


class ProductoAdmin(admin.ModelAdmin):
    pass


class EntradaAdmin(admin.ModelAdmin):
    pass

admin.site.register(UnidadMedida, UnidadMedidaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Entrada, EntradaAdmin)
