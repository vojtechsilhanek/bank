from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  
    path('authentication/', include('authentication.urls')),
    

]
