from django import forms 

class Diposit(forms.Form):
    amount= forms.DecimalField(max_digits=10, required=False)