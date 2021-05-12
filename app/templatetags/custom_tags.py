from django import template

register = template.Library()


@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success'
    return 'bg-danger'
