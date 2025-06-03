from django import forms
from .models import Account, Transactions, Customers

class CustomerForm(forms.ModelForm):
    class Meta:
        fields =  "__all__"
        model = Customers
    

class AccountForm(forms.ModelForm):
    class Meta:
        fields =  "__all__"
        model = Account



class TransactionForm(forms.ModelForm):
    class Meta:
        fields =  "__all__"
        model = Transactions
