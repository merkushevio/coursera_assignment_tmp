from django import template

register = template.Library()


@register.filter
def inc(value, step):
    return int(value) + int(step)


@register.simple_tag
def division(a, b, to_int=True):
    x = int(a)
    y = int(b)
    return x // y if to_int else x / y

