from django.db import models

# Create your models here.
class Gift (models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.category}"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }
