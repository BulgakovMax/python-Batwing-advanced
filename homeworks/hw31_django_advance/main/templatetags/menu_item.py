from django import template
from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu_item_nav.html")
def menu_item():
    return {"menu_item_list": MenuItem.objects.filter().order_by("-name")}