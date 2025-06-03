from django.shortcuts import render, redirect
from .models import Customers, Account, Transactions
from .forms import CustomerForm, AccountForm, TransactionForm

def zobrazit_udaje(request):
    
    zakaznici = Customers.objects.all()
    ucty = Account.objects.all()
    transakce = Transactions.objects.all()

   
    context = {
        'zakaznici': zakaznici,
        'ucty': ucty,
        'transakce': transakce,
    }

    
    return render(request, 'users/index.html', context)


