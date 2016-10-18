from django.shortcuts import render
from django.http import HttpResponse, Http404
from books.models import Book, Publisher
from django.views.generic import ListView
# Create your views here.


def books(request):
    list_books = Book.objects.all()
    return render(request, "books/books.html", {'list_books': list_books})


def book_detail(request, id):
    try:
        id_book = int(id)
    except ValueError:
        raise Http404
    book = Book.objects.get(pk=id_book)
    return render(request, "books/detail.html", {'book': book})


class PublisherList(ListView):
    model = Publisher