from django.apps import AppConfig

class InventarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventario'

    def ready(self):
        # Importar las signals para asegurarse de que se carguen al iniciar la aplicación
        import inventario.signals  # Asegúrate de que el archivo signals.py esté siendo importado
