from django.db import models

# Create your models here.

class Food(models.Model):
    name =models.CharField(max_length=100)
    kitchen_location = models.CharField(max_length=190)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'kitchen_location': self.kitchen_location
        }