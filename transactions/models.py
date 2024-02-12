from django.db import models
from books.models import Book
from django.contrib.auth.models import User


# Create your models here.
class Borrow_report(models.Model):
    user= models.ForeignKey(User,related_name='borrowed', on_delete= models.CASCADE)
    book= models.ForeignKey(Book, on_delete= models.CASCADE)
    borrow_date= models.DateField(auto_now_add=True, null=True, blank=True)
    borrowed_book= models.BooleanField(default=False)
    returned_book= models.BooleanField(default=False)

    
    