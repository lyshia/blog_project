from django.db import models

# Create your models here.

class Dorm(models.Model):
    name = models.CharField(max_length=100)
    current_capacity = models.IntegerField()
    total_capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

   
