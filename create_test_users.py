#!/usr/bin/env python
"""
Script to create test users for the library management system.
Creates one librarian and one member for testing purposes.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
django.setup()

from accounts.models import User

# Create test librarian
if not User.objects.filter(username='librarian1').exists():
    User.objects.create_user(
        username='librarian1',
        email='librarian1@library.com',
        password='librarian123',
        user_type='librarian',
        first_name='John',
        last_name='Doe'
    )
    print("✓ Test librarian created successfully!")
    print("  Username: librarian1")
    print("  Password: librarian123")
    print("  User Type: librarian")
else:
    print("✗ User 'librarian1' already exists!")

print()

# Create test member
if not User.objects.filter(username='member1').exists():
    User.objects.create_user(
        username='member1',
        email='member1@library.com',
        password='member123',
        user_type='member',
        first_name='Jane',
        last_name='Smith'
    )
    print("✓ Test member created successfully!")
    print("  Username: member1")
    print("  Password: member123")
    print("  User Type: member")
else:
    print("✗ User 'member1' already exists!")
