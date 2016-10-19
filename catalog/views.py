from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core import urlresolvers

from cart import carts
from django.http import HttpResponseRedirect
from cart.forms import ProductAddToCartForm

from catalog.models import Category, Product
from website import settings


def custom_processor(request):
    return {
        'app': 'catalog',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR'],
        'site_name': settings.SITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCRIPTION,
    }


def index(request):
    context = custom_processor(request)
    context.update({'products': Product.objects.all()})
    return render(request, 'catalog/index.html', context)


def show_category(request, category_slug):

    context = custom_processor(request)
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    context.update({'products' : products, 'page_title': page_title,
                   'meta_keywords': meta_keywords, 'meta_description': meta_description})
    return render(request, "catalog/category.html", context)


def show_product(request, product_slug):
    context = custom_processor(request);
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description

    context.update({'p': p, 'categories': categories, 'page_title': page_title, 'meta_keywords': meta_keywords,
                    'meta_description': meta_description})

    if request.method == 'POST':
        print "POST method from client!!!!"
        # add to cart...create the bound form
        post_data = request.POST.copy()
        print post_data
        form = ProductAddToCartForm(request, post_data)
        print form.is_valid()

        if form.is_valid():
            # add to cart and redirect to cart page
            carts.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)
    else:
        # it is a GET, create the unbound form. Note request as a kwarg
        form = ProductAddToCartForm(request=request, label_suffix=':')
        # assign the hidden input the product slug
        form.fields['product_slug'].widget.attrs['value'] = product_slug
        # set the test cookie on our first GET request
        request.session.set_test_cookie()
        return render(request, 'catalog/product.html', context)

    return render(request, "catalog/product.html", context)
