from django.urls import path 
from . import views 
urlpatterns = [ 
 path('', views.borrow_list, name='borrow_list'), 
 path('issue/', views.borrow_book, name='borrow_book'),  
 path('<int:pk>/', views.borrow_detail, name='borrow_detail'),  
 path('<int:pk>/return/', views.return_book, name='return_book'), 
]
