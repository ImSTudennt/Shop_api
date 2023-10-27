from django.apps import AppConfig


class MainConfig(AppConfig):
    name = "main"
    verbose_name = "Сервис заказа товаров"

    def ready(self):
        from . import signals
