from django import template
from star_ratings.models import Rating

register = template.Library()


@register.filter
def color(a):
    if a < 2:
        return 'grey'

    elif a == 2:
        return 'yellow'

    elif a == 3:
        return 'green'


@register.filter
def rating_product(pk):
    try:
        star = Rating.objects.get(object_id=pk)
        return star.average
    except Exception as e:
        return 0
