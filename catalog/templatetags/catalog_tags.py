from django import template
from django.contrib.flatpages.models import FlatPage

from cart import carts
from catalog.models import Category

register = template.Library()


@register.inclusion_tag("tags/cart_box.html")
def cart_box_tag(request):
    cart_item_count = carts.cart_distinct_item_count(request)
    return {'cart_item_count': cart_item_count }


@register.inclusion_tag("tags/category_list.html")
def category_list(request_path):
    active_categories = Category.objects.filter(is_active=True)
    return {
        'active_categories': active_categories,
        'request_path': request_path
    }


@register.inclusion_tag("tags/footer.html")
def footer_links():
    flatpage_list = FlatPage.objects.all()
    return {'flatpage_list': flatpage_list }