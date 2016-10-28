from django.conf.urls import include, url
from django.contrib import admin
from website.views import index


urlpatterns = [
      url(r'^admin/', include(admin.site.urls)),
      url(r'^$', index),
      url(r'^books/', include('books.urls')),
      url(r'^catalog/', include('catalog.urls')),
      url(r'^cart/', include('cart.urls')),
      url(r'^pages/', include('django.contrib.flatpages.urls')),
      url(r'^accounts/', include('accounts.urls')),
      url(r'^accounts/', include('django.contrib.auth.urls')),
]
