from django.shortcuts import render
from django.http import HttpResponseRedirect
from cart import carts
from catalog.views import custom_processor
import checkout

def show_cart(request):
    context = custom_processor(request)
    if request.method == 'POST':
        postdata = request.POST.copy()

        if postdata['submit'] == 'Remove':
            carts.remove_from_cart(request)
        if postdata['submit'] == 'Update':
            carts.update_cart(request)
        if postdata['submit'] == 'Checkout':
            checkout_url = checkout.get_checkout_url(request)
            return HttpResponseRedirect(checkout_url)
    cart_items = carts.get_cart_items(request)
    page_title = 'Shopping Cart'
    cart_subtotal = carts.cart_subtotal(request)
    context.update({'cart_items': cart_items, 'page_title': page_title, 'cart_subtotal': cart_subtotal})
    return render(request, "cart/cart.html", context)