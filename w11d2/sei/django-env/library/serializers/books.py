from rest_framework import serializers
from ..models.books import Book

class BookSerializer(serializers.ModelSerializer):
    # define meta
    class Meta:
        model = Book
        fields = "__all__"