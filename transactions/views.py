from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Diposit
from .import models
from users.models import ProfileModel
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.
def send_email(user, transaction, to_email):
    mail_subject="Transaction Message"
    message= render_to_string('email_message.html', {
        "user": user,
        "transaction": transaction,
    })
    send_email= EmailMultiAlternatives(mail_subject,'', to=[to_email] )
    send_email.attach_alternative(message, 'text/html')
    send_email.send()



@login_required
def deposit(request):
    if request.method == 'POST':
        form=Diposit(request.POST)
        if form.is_valid():
            amount= form.cleaned_data['amount']
            account= request.user.account
            account.balance_amount += amount
            account.save()
            messages.success(request,f'{amount} coins has been diposited successfuly')
            send_email(request.user, f'{amount} has been diposited', request.user.email)

            return redirect('home')

    form= Diposit()
    return render(request, 'diposit.html', {'form': form}, )
     
@login_required   
def borrow(request,id):
    this_book= models.Book.objects.get(id=id)    
    our_user= ProfileModel.objects.get(user= request.user)
    # print(our_user)
    # print(our_user.balance_amount)
    
    balance= our_user.balance_amount
    print(balance)
            
    if balance >= this_book.borrow_price:
        our_user.balance_amount -= this_book.borrow_price
        our_user.save()
        messages.success(request, f"Successfully borrowed. Please don't forget to return on time")
        models.Borrow_report.objects.create(
            user= request.user,
            book= this_book,
            borrowed_book= True
        )
        send_email(request.user, f'{this_book.title} has been borrowed', request.user.email)
    else:
        messages.error(request, f"Not enough coins")
    
    
    # return render(request, 'details.html',{'book': this_book} )
    return redirect('details', id=id)

def return_book(request, id):
    this_book= models.Book.objects.get(id=id)
    price= this_book.borrow_price
    print(price)
    our_user= ProfileModel.objects.get(user= request.user)
    our_user.balance_amount += price
    our_user.save()
    print(our_user.balance_amount)
    send_email(request.user, f'{this_book.title} book has been borrowed returned', request.user.email)
    
    models.Borrow_report.objects.filter(user=request.user, book=this_book).update(returned_book=True)
    
    return redirect('profile')

class Show_Borrow_report( LoginRequiredMixin, ListView):
    model= models.Borrow_report
    template_name= 'profile.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset= self.model.objects.filter(user= self.request.user)
        return queryset
    