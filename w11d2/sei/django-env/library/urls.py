# library/urls.py
from django.urls import path

from library.views import authors
from .views import books


urlpatterns = [
    # path('', views.index, name='index'),
    path('books/', books.BooksView.as_view(), name='index'),
    # path('<int:pk>/', views.show, name='Book-detail'),
    path('books/<int:pk>/', books.BookView.as_view(), name='Book-detail'),
    path('authors/', authors.AuthorsView.as_view(), name='index'),
    # path('<int:pk>/', views.show, name='Book-detail'),
    path('authors/<int:pk>/', authors.AuthorView.as_view(), name='Book-detail'),
]
