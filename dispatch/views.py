from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.contrib import messages 
from django.utils import timezone 
from .models import BorrowRecord 
from .forms import BorrowBookForm, ReturnBookForm 
from books.models import Book 
def is_librarian(user): 
 return user.is_authenticated and user.user_type == 'librarian' 
@login_required 
@user_passes_test(is_librarian) 
def borrow_list(request): 
 """List all borrow records""" 
 records = BorrowRecord.objects.all().select_related( 
 'book', 'member', 'member__user' 
 ) 
  
 # Separate active and returned 
 active_borrows = records.filter(return_date__isnull=True)  
 returned_borrows = records.filter(return_date__isnull=False)   
 
 return render(request, 'dispatch/borrow_list.html', { 
  'active_borrows': active_borrows, 
  'returned_borrows': returned_borrows, 
 }) 
@login_required 
@user_passes_test(is_librarian) 
def borrow_book(request): 
 """Issue a book to a member""" 
 if request.method == 'POST': 
  form = BorrowBookForm(request.POST) 
  if form.is_valid(): 
   borrow_record = form.save() 
   # Decrease available copies 
   book = borrow_record.book 
   book.available_copies -= 1 
   book.save() 
   
   messages.success( 
   request,  
   f'{book.title} issued to {borrow_record.member.member_id}'  ) 
   return redirect('borrow_list') 
 else: 
  form = BorrowBookForm() 
  
 return render(request, 'dispatch/borrow_form.html', { 
  'form': form, 
  'title': 'Issue Book' 
 }) 
@login_required 
@user_passes_test(is_librarian) 
def return_book(request, pk): 
 """Process book return""" 
 borrow_record = get_object_or_404(BorrowRecord, pk=pk) 
  
 if borrow_record.return_date: 
  messages.warning(request, 'This book has already been returned.')  
  return redirect('borrow_list') 
  
 if request.method == 'POST':
  form = ReturnBookForm(request.POST, instance=borrow_record)  
  if form.is_valid(): 
   borrow_record = form.save(commit=False) 
   if not borrow_record.return_date: 
    borrow_record.return_date = timezone.now().date()  
   borrow_record.save() 
   
   # Increase available copies 
   book = borrow_record.book 
   book.available_copies += 1 
   book.save() 
   
   messages.success(request, f'{book.title} returned successfully!')  
   return redirect('borrow_list') 
 else: 
  form = ReturnBookForm(instance=borrow_record) 
  form.fields['return_date'].initial = timezone.now().date()   
  
 return render(request, 'dispatch/return_form.html', { 
  'form': form, 
  'borrow_record': borrow_record 
 }) 
@login_required 
def borrow_detail(request, pk): 
 """View borrow record details""" 
 record = get_object_or_404( 
 BorrowRecord.objects.select_related('book', 'member', 'member__user'),  pk=pk 
 ) 
 return render(request, 'dispatch/borrow_detail.html', {'record': record})
