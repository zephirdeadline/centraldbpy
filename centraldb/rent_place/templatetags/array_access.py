from django import template

register = template.Library()


@register.filter
def index(l, i):
    return l[i]


@register.filter
def field(o, attr):
    return getattr(o, attr)
