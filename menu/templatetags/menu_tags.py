from django import template
from django.urls import reverse
from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def drev_menu(context, menu_name):
    curent_url = reverse(context['request'].path.info).url_name
    menus_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    menu_tree = _build_tree(menus_items, curent_url)
    return _render_menu(menu_tree)


def _build_tree(menu_items, curent_url):
    tree = []
    items_dict = {item.id: item for item in menu_items}
    for item in menu_items:
        item.is_active = (curent_url == item.named_url or curent_url == item.url)
        if item.parent_id:
            parent = items_dict.get(item.parent_id)
            if not hasattr(parent, 'children_list'):
                parent.children_list = []
            parent.children_list.append(item)
        else:
            tree.append(item)
    return tree


def _render_menu(menu_items, level=0):
    if not menu_items:
        return ''

    output = '<ul>'
    for item in menu_items:
        output += f"<li>{item.name}"
        if hasattr(item, 'children_list'):
            output += _render_menu(item.children_list, level + 1)
        output += "</li>"
    output += '</ul>'

    return output