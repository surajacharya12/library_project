from django.urls import path 
from . import views 
urlpatterns = [ 
 # Librarian URLs 
 path('', views.book_list, name='book_list'), 
 path('add/', views.book_create, name='book_create'), 
 path('<int:pk>/', views.book_detail, name='book_detail'), 
 path('<int:pk>/edit/', views.book_update, name='book_update'),  
 path('<int:pk>/delete/', views.book_delete, name='book_delete'),   
 # Member URLs 
 path('available/', views.available_books, name='available_books'),  
 path('my-books/', views.member_borrowed_books, name='member_borrowed_books'), 
]
