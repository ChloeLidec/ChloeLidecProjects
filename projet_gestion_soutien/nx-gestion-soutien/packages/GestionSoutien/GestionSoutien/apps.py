from django.apps import AppConfig
from django.db import connection
import sys

class GestionsoutienConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GestionSoutien'
    verbose_name = "Gestion du soutien"
    
    def ready(self):
        # Vérifier si la commande actuelle est liée aux migrations
        if 'migrate' not in sys.argv and 'makemigrations' not in sys.argv:
            # La commande actuelle n'est pas liée à une migration, appelez start()
            from .scheduler.scheduler import start
            start()
