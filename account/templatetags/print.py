from django import template

register = template.Library()


@register.filter
def log(value):
    print(value)


@register.filter
def log_type(value):
    print(type(value))