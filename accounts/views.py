from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    """
    Handle user login.
    GET: Display login form
    POST: Process login credentials
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login successful
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            
            # Redirect based on user type
            if user.is_librarian():
                return redirect('librarian_dashboard')
            else:
                return redirect('member_dashboard')
        else:
            # Login failed
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')

@login_required
def librarian_dashboard(request):
    """
    Dashboard for librarians.
    """
    return render(request, 'accounts/librarian_dashboard.html')

@login_required
def member_dashboard(request):
    """
    Dashboard for members.
    """
    return render(request, 'accounts/member_dashboard.html')
