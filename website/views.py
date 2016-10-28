from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'site_name': 'Modern Musician'})


def catalog(request):
    return render(request, 'catalog.html', {'site_name': 'Modern Musician'})