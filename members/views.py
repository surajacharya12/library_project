from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.contrib import messages 
from .models import Member 
from .forms import MemberRegistrationForm, MemberUpdateForm 
def is_librarian(user): 
 return user.is_authenticated and user.user_type == 'librarian' 
@login_required 
@user_passes_test(is_librarian) 
def member_list(request): 
 members = Member.objects.all() 
 return render(request, 'members/member_list.html', {'members': members}) 
@login_required 
@user_passes_test(is_librarian) 
def member_create(request): 
 if request.method == 'POST': 
  form = MemberRegistrationForm(request.POST) 
  if form.is_valid(): 
   form.save() 
   messages.success(request, 'Member registered successfully!')  
   return redirect('member_list') 
 else: 
  form = MemberRegistrationForm() 
  
 return render(request, 'members/member_form.html', { 
  'form': form, 
  'title': 'Register New Member' 
 }) 
@login_required 
def member_detail(request, pk): 
 member = get_object_or_404(Member, pk=pk) 
 return render(request, 'members/member_detail.html', {'member': member}) 
@login_required 
@user_passes_test(is_librarian) 
def member_update(request, pk): 
 member = get_object_or_404(Member, pk=pk) 
  
 if request.method == 'POST': 
  form = MemberUpdateForm(request.POST, instance=member)  
  if form.is_valid(): 
   form.save() 
   messages.success(request, 'Member updated successfully!')  
   return redirect('member_detail', pk=member.pk) 
 else: 
  form = MemberUpdateForm(instance=member) 
  
 return render(request, 'members/member_form.html', { 
  'form': form, 
  'title': 'Update Member', 
  'member': member 
 }) 
@login_required 
@user_passes_test(is_librarian) 
def member_delete(request, pk): 
 member = get_object_or_404(Member, pk=pk) 
  
 if request.method == 'POST': 
  user = member.user 
  member.delete() 
  user.delete() # Also delete the user account
  messages.success(request, 'Member deleted successfully!')  
  return redirect('member_list') 
  
 return render(request, 'members/member_confirm_delete.html',   {'member': member})
