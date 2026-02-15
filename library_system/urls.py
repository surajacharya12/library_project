
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect 

def home(request): 
    return render(request, 'accounts/home.html') 

urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('accounts/', include('accounts.urls')), 
    path('books/', include('books.urls')), 
    path('members/', include('members.urls')), 
    path('dispatch/', include('dispatch.urls')), 
    path('', home, name='home'), 
]
