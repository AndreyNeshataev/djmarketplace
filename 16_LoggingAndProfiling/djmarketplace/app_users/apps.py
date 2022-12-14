from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_users'
    verbose_name = _('Пользователь')
    verbose_name_plural = _('Пользователи')
