from rest_framework import serializers
from ..models.authors import Author
from ..serializers.books import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)

    class Meta:

        model = Author
        fields = ["id", "first_name", "last_name", "books"]