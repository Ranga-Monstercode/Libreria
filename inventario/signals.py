from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Producto, InventarioBodega

@receiver(post_save, sender=Producto)
def crear_inventario_bodega(sender, instance, created, **kwargs):
    # Solo ejecutamos esto si el producto fue creado (no actualizado)
    if created:
        # Obtener la bodega asociada al producto
        bodega = instance.bodega
        
        # Verificar si hay una bodega asociada
        if bodega:
            # Crear el registro en InventarioBodega
            InventarioBodega.objects.create(producto=instance, bodega=bodega)
