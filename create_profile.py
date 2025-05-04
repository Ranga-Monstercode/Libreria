import os
import django

# Configurar entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libreria.settings')
django.setup()

from django.contrib.auth.models import User
from inventario.models import Perfil

# Obtener el superusuario (asumiendo que solo hay uno)
superuser = User.objects.filter(is_superuser=True).first()

if superuser:
    # Verificar si ya tiene un perfil
    try:
        perfil = Perfil.objects.get(usuario=superuser)
        print(f"El usuario {superuser.username} ya tiene un perfil con rol: {perfil.get_rol_display()}")
    except Perfil.DoesNotExist:
        # Crear perfil de administrador para el superusuario
        perfil = Perfil.objects.create(
            usuario=superuser,
            rol='administrador'
        )
        print(f"Se ha creado un perfil de administrador para {superuser.username}")
else:
    print("No se encontró ningún superusuario en el sistema")