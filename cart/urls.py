from django.conf.urls import url

from cart.views import show_cart

urlpatterns = [
      url(r'^$', show_cart, name='show_cart'),
]
