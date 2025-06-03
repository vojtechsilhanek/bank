from django.urls import path
from . import views

urlpatterns = [
    path('', views.zobrazit_udaje, name='zobrazit_udaje'),
    
]
