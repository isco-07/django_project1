from django import template

register = template.Library()


@register.filter()
def mimedia(val):
    if val:
        return f'/media/{val}'
    return '#'
