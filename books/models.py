from django.db import models 
from django.core.validators import MinValueValidator 
class Book(models.Model): 
 """ 
 Model representing a book in the library. 
 """ 
 title = models.CharField( 
 max_length=200, 
 help_text="Enter the book title" 
 ) 
  
 author = models.CharField( 
 max_length=100, 
 help_text="Enter the author's name" 
 ) 
  
 isbn = models.CharField( 
 max_length=13, 
 unique=True, 
 help_text="13 Character ISBN number" 
 ) 
  
 publisher = models.CharField( 
 max_length=100, 
 blank=True, 
 help_text="Publisher name (optional)" 
 ) 
  
 publication_year = models.IntegerField( 
 validators=[MinValueValidator(1000)], 
 help_text="Year of publication" 
 ) 
  
 category = models.CharField( 
 max_length=50, 
 choices=[ 
 ('fiction', 'Fiction'), 
 ('non_fiction', 'Non-Fiction'), 
 ('science', 'Science'), 
 ('history', 'History'), 
 ('biography', 'Biography'), 
 ('children', 'Children'), 
 ('reference', 'Reference'), 
 ], 
 default='fiction' 
 ) 
  
 total_copies = models.IntegerField( 
 default=1, 
 validators=[MinValueValidator(1)], 
 help_text="Total number of copies" 
 ) 
  
 available_copies = models.IntegerField( 
 default=1, 
 validators=[MinValueValidator(0)], 
 help_text="Number of copies available for borrowing"  ) 
  
 description = models.TextField( 
 blank=True,
 help_text="Brief description of the book"  ) 
  
 added_date = models.DateTimeField(auto_now_add=True)  
 updated_date = models.DateTimeField(auto_now=True)   
 
 class Meta: 
  ordering = ['title'] 
  verbose_name = 'Book' 
  verbose_name_plural = 'Books' 
  
 def __str__(self): 
  return f"{self.title} by {self.author}"   
  
 def is_available(self): 
  """Check if book is available for borrowing"""  
  return self.available_copies > 0
