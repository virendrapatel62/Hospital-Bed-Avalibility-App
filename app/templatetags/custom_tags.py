from app.models import Availability
from django import template

register = template.Library()


@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success'
    return 'bg-danger'


@register.simple_tag
def get_availibilities(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')


@register.simple_tag
def is_state_selected(selected_state, pk):
    print(pk, selected_state)
    if selected_state == str(pk):
        return 'selected'
    return ''


@register.simple_tag
def is_city_selected(selected_city_id, pk):

    if selected_city_id == str(pk):
        return 'selected'
    return ''
