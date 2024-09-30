from django.apps import AppConfig
from django.utils import timezone


class ResultsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'football_site.results'

    def ready(self):
        from ..update_files.pl_fixtures import pl_fixtures
        from ..update_files.laliga_fixtures import laliga_fixtures
        # from ..update_files.laliga_fixtures_update import update_laliga_fixtures
        # from ..update_files.pl_fixtures_update import update_pl_fixtures
        # from ..update_files.fetch_laliga import la_liga_update # to delete
        # from ..update_files.fetch_pl import pl_update # to delete

        pl_fixtures()
        laliga_fixtures()
        # update_pl_fixtures()
        # update_laliga_fixtures()
        # la_liga_update()
        # pl_update()
        print(timezone.now())

        
