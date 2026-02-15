from django.db import models 
from django.utils import timezone 
from datetime import timedelta 
from books.models import Book 
from members.models import Member 
class BorrowRecord(models.Model): 
 """ 
 Model representing a book borrowing record. 
 """ 
 book = models.ForeignKey( 
 Book, 
 on_delete=models.CASCADE, 
 help_text="Book being borrowed" 
 ) 
  
 member = models.ForeignKey( 
 Member, 
 on_delete=models.CASCADE, 
 help_text="Member borrowing the book" 
 ) 
  
 borrow_date = models.DateTimeField( 
 auto_now_add=True, 
 help_text="Date and time when book was borrowed" 
 ) 
  
 due_date = models.DateField( 
 help_text="Date when book should be returned" 
 ) 
  
 return_date = models.DateField( 
 null=True, 
 blank=True, 
 help_text="Actual return date (null if not returned)"  ) 
  
 STATUS_CHOICES = [ 
 ('borrowed', 'Borrowed'), 
 ('returned', 'Returned'), 
 ('overdue', 'Overdue'), 
 ] 
  
 status = models.CharField( 
 max_length=20, 
 choices=STATUS_CHOICES, 
 default='borrowed' 
 ) 
  
 notes = models.TextField( 
 blank=True, 
 help_text="Additional notes" 
 ) 
  
 class Meta: 
  ordering = ['-borrow_date'] 
  verbose_name = 'Borrow Record' 
  verbose_name_plural = 'Borrow Records' 
  
 def __str__(self): 
  return f"{self.book.title} - {self.member.member_id}"   
  
 def save(self, *args, **kwargs): 
  # Set due date if not provided (14 days from now)  
  if not self.due_date: 
   self.due_date = (timezone.now() + timedelta(days=14)).date() 
   
  # Update status based on dates 
  if self.return_date: 
   self.status = 'returned' 
  elif timezone.now().date() > self.due_date: 
   self.status = 'overdue' 
  else: 
   self.status = 'borrowed' 
   
  super().save(*args, **kwargs) 
  
 def is_overdue(self): 
  """Check if book is overdue""" 
  if self.return_date: 
   return False 
  return timezone.now().date() > self.due_date   
  
 def days_borrowed(self): 
  """Calculate days book has been borrowed""" 
  if self.return_date: 
   return (self.return_date - self.borrow_date.date()).days  
  return (timezone.now().date() - self.borrow_date.date()).days
