from django.conf.urls import url
from django.contrib.auth import views as auth_views

from views import my_account, order_details, order_info, register


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^my_account/$', my_account, name='my_account'),
    url(r'^order_details/(?P<order_id>[-\w]+)/$', order_details, name='order_details'),
    url(r'^order_info/$', order_info, name='order_info'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
