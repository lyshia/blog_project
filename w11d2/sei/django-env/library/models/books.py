from django.db import models

from .authors import Author

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name = "books", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    