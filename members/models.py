from django.db import models 
from django.contrib.auth import get_user_model 
User = get_user_model() 
class Member(models.Model): 
 """ 
 Model representing a library member who can borrow books.  """ 
 user = models.OneToOneField( 
 User, 
 on_delete=models.CASCADE, 
 limit_choices_to={'user_type': 'member'}, 
 help_text="Link to user account" 
 ) 
  
 member_id = models.CharField( 
 max_length=20, 
 unique=True, 
 help_text="Unique member ID" 
 ) 
  
 phone_number = models.CharField( 
 max_length=15, 
 help_text="Contact phone number" 
 ) 
  
 address = models.TextField( 
 help_text="Residential address" 
 ) 
  
 date_of_birth = models.DateField( 
 help_text="Date of birth" 
 ) 
  
 membership_date = models.DateField( 
 auto_now_add=True, 
 help_text="Date of membership registration" 
 ) 
  
 is_active = models.BooleanField( 
 default=True, 
 help_text="Is membership active?" 
 ) 
  
 class Meta: 
  ordering = ['member_id'] 
  verbose_name = 'Member' 
  verbose_name_plural = 'Members' 
  
 def __str__(self): 
  return f"{self.member_id} - {self.user.get_full_name()}"   
  
 def get_borrowed_books_count(self): 
  """Get count of currently borrowed books""" 
  return self.borrowrecord_set.filter(return_date__isnull=True).count()
