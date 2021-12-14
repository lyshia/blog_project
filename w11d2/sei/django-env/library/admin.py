from django.contrib import admin

from .models.authors import Author
from .models.books import Book
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)