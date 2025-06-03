from django.contrib import admin
from .models import Customers, Account, Transactions

# Registrace modelů
admin.site.register(Customers)
admin.site.register(Account)
admin.site.register(Transactions)
