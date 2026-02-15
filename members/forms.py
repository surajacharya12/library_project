from django import forms 
from django.contrib.auth import get_user_model 
from .models import Member 
User = get_user_model() 
class MemberRegistrationForm(forms.ModelForm): 
 """Form for registering new members""" 
 # User fields 
 username = forms.CharField(max_length=150) 
 first_name = forms.CharField(max_length=30) 
 last_name = forms.CharField(max_length=30) 
 email = forms.EmailField() 
 password = forms.CharField(widget=forms.PasswordInput) 
 confirm_password = forms.CharField(widget=forms.PasswordInput)   
 
 class Meta: 
  model = Member 
  fields = ['member_id', 'phone_number', 'address', 'date_of_birth']  
  widgets = { 
  'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  
  'address': forms.Textarea(attrs={'rows': 3}), 
  } 
 
 def clean_username(self): 
  """Validate that the username is unique."""
  username = self.cleaned_data.get('username') 
  if User.objects.filter(username=username).exists(): 
   raise forms.ValidationError("Username already exists. Please choose a different one.") 
  return username

 def clean(self): 
  # Standard clean logic to ensure passwords match
  cleaned_data = super().clean() 
  password = cleaned_data.get('password') 
  confirm_password = cleaned_data.get('confirm_password')   
  if password != confirm_password: 
   raise forms.ValidationError("Passwords do not match!")   
  return cleaned_data 
  
 def save(self, commit=True): 
  # Create user account first 
  user = User.objects.create_user( 
  username=self.cleaned_data['username'], 
  email=self.cleaned_data['email'], 
  password=self.cleaned_data['password'], 
  first_name=self.cleaned_data['first_name'], 
  last_name=self.cleaned_data['last_name'], 
  user_type='member' 
  ) 
  
  # Create member profile 
  member = super().save(commit=False) 
  member.user = user 
  if commit: 
   member.save() 
  return member 
class MemberUpdateForm(forms.ModelForm): 
 """Form for updating member information""" 
 first_name = forms.CharField(max_length=30) 
 last_name = forms.CharField(max_length=30) 
 email = forms.EmailField() 
  
 class Meta: 
  model = Member 
  fields = ['phone_number', 'address', 'is_active'] 
  widgets = { 
  'address': forms.Textarea(attrs={'rows': 3}), 
  } 
  
 def __init__(self, *args, **kwargs):
  super().__init__(*args, **kwargs) 
  if self.instance and self.instance.user: 
   self.fields['first_name'].initial = self.instance.user.first_name  
   self.fields['last_name'].initial = self.instance.user.last_name  
   self.fields['email'].initial = self.instance.user.email   
   
 def save(self, commit=True): 
  member = super().save(commit=False) 
  # Update user information 
  user = member.user 
  user.first_name = self.cleaned_data['first_name'] 
  user.last_name = self.cleaned_data['last_name'] 
  user.email = self.cleaned_data['email'] 
  user.save() 
  
  if commit: 
   member.save() 
  return member
