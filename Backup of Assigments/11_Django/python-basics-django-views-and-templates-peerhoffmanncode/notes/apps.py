from django.apps import AppConfig

from django.template import Library
from .templatetags.filters import linkable_section

register = Library()
register.filter(linkable_section)


class NotesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "notes"
