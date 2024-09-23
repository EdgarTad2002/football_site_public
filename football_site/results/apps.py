from django.apps import AppConfig


class ResultsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'football_site.results'

    def ready(self):
        from ..update_files.pl_fixtures import pl_fixtrues
        pl_fixtrues()

        
