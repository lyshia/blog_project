from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.books import BookSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.books import Book


# /books

class BooksView(APIView):
    # POST / books
    def post(self, request):
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()
            return Response(book.data, status=status.HTTP_201_CREATED)
        else:
            return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET /books
    def get(self, request):
        books = Book.objects.all()
        data = BookSerializer(books, many=True).data
        return Response(data)
      

class BookView(APIView):
    # GET /books/:id
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        data = BookSerializer(book).data
        return Response(data)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        updated_book = BookSerializer(book, data=request.data)
        if updated_book.is_valid():
            updated_book.save()
            return Response(updated_book.data)

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        updated_book = BookSerializer(book, data=request.data, partial = True)
        if updated_book.is_valid():
            updated_book.save()
            return Response(updated_book.data)