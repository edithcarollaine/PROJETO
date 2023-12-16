from django.apps import AppConfig


class AppProjetoSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_projeto_site'

    def ready(self):
        import app_projeto_site.signals