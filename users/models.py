from django.db import models
from django.contrib.auth.models import User
# # Create your models here.
from books.models import Book

class ProfileModel(models.Model):
    user= models.OneToOneField(User,related_name='account', on_delete= models.CASCADE)
    balance_amount= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # borrowed_books= models.ManyToManyField(Book)
    
    def __str__(self) -> str:
        return self.user.username



    
