from django.db import models
from django.contrib.auth.models import User
from .import constants

# Create your models here.

class Category(models.Model):
    title= models.CharField(max_length= 20)
    
    def __str__(self) -> str:
        return self.title

class Book(models.Model):
    title= models.CharField(max_length= 40, unique=True)
    image= models.ImageField(upload_to='books/media')
    description= models.TextField()
    categories= models.ManyToManyField(Category)
    borrow_price= models.DecimalField(max_digits=20, decimal_places=2)
    
    def __str__(self) -> str:
        return self.title
    
class Review(models.Model):
    rate= models.IntegerField(choices= constants.RATE_CHOICES)
    user= models.OneToOneField(User, on_delete= models.CASCADE,related_name='review')
    book= models.ForeignKey(Book,on_delete= models.CASCADE, related_name='review')
    
    def __str__(self) -> str:
        return f"{self.user.username}'s review"