from django.apps import AppConfig


class TagAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tag_app'

    def ready(self):
        import tag_app.signals  # noqa
