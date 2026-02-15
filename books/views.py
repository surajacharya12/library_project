from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.contrib import messages 
from django.db.models import Q
from .models import Book 
from .forms import BookForm 
from dispatch.models import BorrowRecord
def is_librarian(user): 
 return user.is_authenticated and user.user_type == 'librarian' 
@login_required 
@user_passes_test(is_librarian) 
def book_list(request): 
 """Display all books""" 
 books = Book.objects.all() 
 return render(request, 'books/book_list.html', {'books': books}) 
@login_required 
@user_passes_test(is_librarian) 
def book_create(request): 
 """Create a new book""" 
 if request.method == 'POST': 
  form = BookForm(request.POST) 
  if form.is_valid(): 
   form.save() 
   messages.success(request, 'Book added successfully!')  
   return redirect('book_list') 
 else: 
  form = BookForm() 
  
 return render(request, 'books/book_form.html', { 
  'form': form, 
  'title': 'Add New Book' 
 }) 
@login_required 
def book_detail(request, pk): 
 """Display book details""" 
 book = get_object_or_404(Book, pk=pk) 
 return render(request, 'books/book_detail.html', {'book': book}) 
@login_required 
@user_passes_test(is_librarian) 
def book_update(request, pk): 
 """Update an existing book""" 
 book = get_object_or_404(Book, pk=pk) 
  
 if request.method == 'POST': 
  form = BookForm(request.POST, instance=book) 
  if form.is_valid(): 
   form.save() 
   messages.success(request, 'Book updated successfully!')  
   return redirect('book_detail', pk=book.pk) 
 else: 
  form = BookForm(instance=book) 
  
 return render(request, 'books/book_form.html', { 
  'form': form, 
  'title': 'Edit Book', 
  'book': book 
 }) 
@login_required 
@user_passes_test(is_librarian) 
def book_delete(request, pk): 
 """Delete a book"""
 book = get_object_or_404(Book, pk=pk) 
  
 if request.method == 'POST': 
  book.delete() 
  messages.success(request, 'Book deleted successfully!')  
  return redirect('book_list') 
  
 return render(request, 'books/book_confirm_delete.html', {'book': book})
