
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')), 
    path('members/', include('members.urls')), 
    path('', lambda request: redirect('login')),  # Redirect root to login
]
