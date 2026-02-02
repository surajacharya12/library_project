from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for User model.
    Extends Django's built-in UserAdmin.
    """
    # Fields to display in the user list
    list_display = ['username', 'email', 'user_type', 'is_staff', 'is_active']
    
    # Filters in the sidebar
    list_filter = ['user_type', 'is_staff', 'is_active']
    
    # Search functionality
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    # Add user_type to the fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('user_type',)}),
    )
    
    # Add user_type when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('user_type',)}),
    )
