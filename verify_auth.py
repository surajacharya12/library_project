#!/usr/bin/env python
"""
Script to verify the authentication system is working correctly.
This script tests the user model and authentication functionality.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
django.setup()

from accounts.models import User
from django.contrib.auth import authenticate

print("=" * 60)
print("AUTHENTICATION SYSTEM VERIFICATION")
print("=" * 60)

# Test 1: Verify users exist
print("\n1. Checking if users exist...")
admin = User.objects.filter(username='admin').first()
librarian = User.objects.filter(username='librarian1').first()
member = User.objects.filter(username='member1').first()

if admin:
    print(f"   ✓ Admin user exists: {admin} - Type: {admin.user_type}")
else:
    print("   ✗ Admin user not found!")

if librarian:
    print(f"   ✓ Librarian user exists: {librarian} - Type: {librarian.user_type}")
else:
    print("   ✗ Librarian user not found!")

if member:
    print(f"   ✓ Member user exists: {member} - Type: {member.user_type}")
else:
    print("   ✗ Member user not found!")

# Test 2: Verify authentication
print("\n2. Testing authentication...")
auth_librarian = authenticate(username='librarian1', password='librarian123')
if auth_librarian:
    print(f"   ✓ Librarian authentication successful")
else:
    print("   ✗ Librarian authentication failed!")

auth_member = authenticate(username='member1', password='member123')
if auth_member:
    print(f"   ✓ Member authentication successful")
else:
    print("   ✗ Member authentication failed!")

# Test 3: Verify helper methods
print("\n3. Testing user type helper methods...")
if librarian:
    print(f"   librarian1.is_librarian(): {librarian.is_librarian()}")
    print(f"   librarian1.is_member(): {librarian.is_member()}")

if member:
    print(f"   member1.is_librarian(): {member.is_librarian()}")
    print(f"   member1.is_member(): {member.is_member()}")

# Test 4: List all users
print("\n4. All users in the system:")
all_users = User.objects.all()
for user in all_users:
    print(f"   - {user.username}: {user.user_type} (Staff: {user.is_staff}, Superuser: {user.is_superuser})")

print("\n" + "=" * 60)
print("VERIFICATION COMPLETE!")
print("=" * 60)
print("\nYou can now test the web interface at: http://127.0.0.1:8000/")
print("\nTest Accounts:")
print("  1. Admin (Superuser):")
print("     Username: admin")
print("     Password: admin123")
print("\n  2. Librarian:")
print("     Username: librarian1")
print("     Password: librarian123")
print("\n  3. Member:")
print("     Username: member1")
print("     Password: member123")
print("=" * 60)
