from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from .import models
from .import forms

# Create your views here.
def home(request):
    books= models.Book.objects.all()
    categories= models.Category.objects.all()
    return render(request, 'home.html', {'books': books, 'categories': categories, 'var':'none'})

def sort_cat(request, id):
    cat= models.Category.objects.get(pk=id)
    books= models.Book.objects.filter(categories=cat)
    categories= models.Category.objects.all()
    return render(request, 'home.html', {'books': books, 'categories': categories, 'var':'sort'})
    
class Detail(DetailView):
    model= models.Book
    pk_url_kwarg= 'id'
    template_name='details.html'
    
    def post(self, request, *args, **kwargs):
        review_form= forms.ReviewForm(request.POST)
        book= self.get_object()
        
        if review_form.is_valid():
            review= review_form.save(commit=False)
            review.user= self.request.user
            review.book= book 
            review.save()
            return redirect('details', id= book.id)
        
        # return self.get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        book= self.get_object()
        form= forms.ReviewForm()
        review= book.review.all()
        
        context['form']= form
        context['review']= review
        
        return context
        