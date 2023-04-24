
# Create your models here.

from django.db import models


class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    pages=models.IntegerField()

    def __str__(self):
        return self.name