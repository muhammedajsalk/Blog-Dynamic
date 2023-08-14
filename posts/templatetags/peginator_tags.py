from django import template
from django.core.paginator import Paginator


register = template.Library()

@register.simple_tag
def get_elided_page_range(instances, number, on_each_side=3, on_ends=2):
    paginator =Paginator(instances.object_list, instances.per_page)
    return paginator.get_elided_page_range(number=number, on_each_side=on_each_side, on_ends=on_ends)