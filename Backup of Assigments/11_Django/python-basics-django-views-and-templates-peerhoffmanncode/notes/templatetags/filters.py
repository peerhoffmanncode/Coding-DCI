from django import template
from django.urls import reverse

register = template.Library()


@register.filter
def linkable_section(text):
    return f'<a href="{reverse("notes:by_section", kwargs={"section_name":text})}">{text}</a>'
