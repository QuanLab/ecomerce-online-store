from django.conf.urls import url
from books.views import PublisherList, books, book_detail


urlpatterns = [
      url(r'^$', books),
      url(r'(\d{1,2})/$', book_detail),
      url(r'^publishers/$', PublisherList.as_view()),
]
