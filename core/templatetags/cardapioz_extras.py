from django import template

register = template.Library()


@register.filter
def color(a):
    if a < 2:
        return 'grey'

    elif a == 2:
        return 'yellow'

    elif a == 3:
        return 'green'
