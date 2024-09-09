from django import template
from menu_tree.models import Menu

register = template.Library()


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu):
    request = context['request']
    current_url = request.path
    menu = Menu.objects.get(name=menu)
    menu_items = menu.items.all()

    def build_menu_tree(parent=None):
        items = []
        for item in menu_items.filter(parent=parent).order_by('order'):
            items.append({
                'item': item,
                'children': build_menu_tree(item),
                'is_active': current_url.startswith(item.url),
            })
        return items

    menu_tree = build_menu_tree()

    return {
        'menu_tree': menu_tree,
        'current_url': current_url,
    }
