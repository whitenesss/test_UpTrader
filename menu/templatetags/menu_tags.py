from django import template
from menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent')

    # Определение активного пункта меню по URL
    active_item = None
    for item in menu_items:
        if request.path == item.get_url():
            active_item = item
            break

    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_tree(items, parent=item)
                tree.append({'item': item, 'children': children, 'is_active': item == active_item})
        return tree

    # Построение дерева меню
    menu_tree = build_tree(menu_items)
    return {'menu_tree': menu_tree, 'active_item': active_item}
