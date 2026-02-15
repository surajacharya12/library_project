from django import forms 
from .models import Book 
class BookForm(forms.ModelForm): 
 """ 
 Form for creating and editing books. 
 """ 
 class Meta: 
  model = Book 
  fields = ['title', 'author', 'isbn', 'publisher',   'publication_year', 'category', 'total_copies',   'available_copies', 'description'] 
  
  widgets = { 
  'title': forms.TextInput(attrs={ 
  'class': 'form-control', 
  'placeholder': 'Enter book title' 
  }), 
  'author': forms.TextInput(attrs={ 
  'class': 'form-control', 
  'placeholder': 'Enter author name' 
  }), 
  'isbn': forms.TextInput(attrs={ 
  'class': 'form-control', 
  'placeholder': '13-digit ISBN' 
  }), 
  'publisher': forms.TextInput(attrs={ 
  'class': 'form-control', 
  'placeholder': 'Publisher name (optional)'  }), 
  'publication_year': forms.NumberInput(attrs={  'class': 'form-control', 
  'min': '1000', 
  'max': '2100' 
  }), 
  'category': forms.Select(attrs={ 
  'class': 'form-control' 
  }), 
  'total_copies': forms.NumberInput(attrs={  'class': 'form-control', 
  'min': '1' 
  }), 
  'available_copies': forms.NumberInput(attrs={  'class': 'form-control', 
  'min': '0' 
  }), 
  'description': forms.Textarea(attrs={ 
  'class': 'form-control', 
  'rows': '4', 
  'placeholder': 'Brief description (optional)'  }), 
  } 
  
 def clean(self): 
  cleaned_data = super().clean() 
  total = cleaned_data.get('total_copies') 
  available = cleaned_data.get('available_copies')   
  
  if total and available and available > total:  
   raise forms.ValidationError( 
   "Available copies cannot exceed total copies."  
   ) 
  
  return cleaned_data
