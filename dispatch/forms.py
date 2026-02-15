from django import forms 
from .models import BorrowRecord 
from books.models import Book 
from members.models import Member 
class BorrowBookForm(forms.ModelForm): 
 """Form for borrowing a book""" 
 class Meta: 
  model = BorrowRecord 
  fields = ['book', 'member', 'due_date', 'notes']  
  widgets = { 
  'due_date': forms.DateInput(attrs={'type': 'date'}),  
  'notes': forms.Textarea(attrs={'rows': 3}),  
  } 
  
 def __init__(self, *args, **kwargs): 
  super().__init__(*args, **kwargs) 
  # Only show available books 
  self.fields['book'].queryset = Book.objects.filter(  available_copies__gt=0 
  ) 
  # Only show active members 
  self.fields['member'].queryset = Member.objects.filter(  is_active=True 
  ) 
  
 def clean(self): 
  cleaned_data = super().clean() 
  book = cleaned_data.get('book') 
  
  if book and book.available_copies < 1: 
   raise forms.ValidationError( 
   f"{book.title} is not available for borrowing."  
   ) 
  return cleaned_data 
class ReturnBookForm(forms.ModelForm): 
 """Form for returning a book""" 
 class Meta: 
  model = BorrowRecord 
  fields = ['return_date', 'notes'] 
  widgets = { 
  'return_date': forms.DateInput(attrs={'type': 'date'}),  
  'notes': forms.Textarea(attrs={'rows': 3}),  
  }
