from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.shortcuts import render
from django.contrib.auth import authenticate, login

import datetime


def index(request):
    return render(request, 'index.html', {'site_name': 'Modern Musician'})


def catalog(request):
    return render(request, 'catalog.html', {'site_name': 'Modern Musician'})


def current_datetime(request):

    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be  %s." % (offset, dt)
    return HttpResponse(html)