from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from checkout.models import Order, OrderItem
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        print postdata
        form = UserCreationForm(postdata)
        if form.is_valid():
            form.save()
            un = postdata.get('username','')
            pw = postdata.get('password1','')
            from django.contrib.auth import login, authenticate
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = urlresolvers.reverse('my_account')
                print url
                return HttpResponseRedirect(url)
    else:
        form = UserCreationForm()
    page_title = 'User Registration'
    return render(request, 'registration/register.html', {'page_title':page_title, 'form': form})


@login_required
def my_account(request):
    page_title = 'My Account'
    orders = Order.objects.filter(user=request.user)
    name = request.user.username
    context = {'page_title': page_title, 'orders':orders, 'name': name}
    return render(request, "registration/my_account.html", context)


def order_details(request):
    return ""


def order_info(request):
    return ""


def login(request):
    return ""