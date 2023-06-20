
# Create your models here.

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator

class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    pages=models.IntegerField()

    def __str__(self):
        return self.name

class user(models.Model):
    user=models.CharField(primary_key=True,max_length=20)
 


class items(models.Model):
    product=models.CharField(max_length=20)
    arrived=models.DateTimeField(auto_now_add=True)
    shipped=models.DateField(auto_now_add=True)
    expiry = models.DateField()
    owner=models.ForeignKey(user, on_delete=models.CASCADE)


class profile(models.Model):
    owner=models.ForeignKey(user, on_delete=models.CASCADE)
    age=models.IntegerField(validators=[MinValueValidator(0,message="Please enter your correct age."), MaxValueValidator(150,message="Please enter your correct age.")])
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Phone number must be a 10-digit number.'
            )
        ]
    )
    address = models.TextField()
