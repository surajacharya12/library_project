#!/usr/bin/env python
"""
Script to create a superuser for the library management system.
This creates an admin account with librarian privileges.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
django.setup()

from accounts.models import User

# Create superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@library.com',
        password='admin123',
        user_type='librarian'
    )
    print("✓ Superuser 'admin' created successfully!")
    print("  Username: admin")
    print("  Password: admin123")
    print("  User Type: librarian")
else:
    print("✗ Superuser 'admin' already exists!")
