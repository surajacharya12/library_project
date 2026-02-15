from django.contrib import admin 
from .models import Book 
@admin.register(Book) 
class BookAdmin(admin.ModelAdmin): 
 list_display = ['title', 'author', 'isbn', 'category',   'available_copies', 'total_copies', 'is_available']  
 list_filter = ['category', 'publication_year'] 
 search_fields = ['title', 'author', 'isbn'] 
 readonly_fields = ['added_date', 'updated_date'] 
  
 fieldsets = ( 
 ('Basic Information', { 
 'fields': ('title', 'author', 'isbn', 'category')  }), 
 ('Publication Details', { 
 'fields': ('publisher', 'publication_year', 'description')  }), 
 ('Inventory', { 
 'fields': ('total_copies', 'available_copies')  }), 
 ('Metadata', { 
 'fields': ('added_date', 'updated_date'), 
 'classes': ('collapse',) 
 }), 
 )
