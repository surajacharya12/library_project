from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Adds a user_type field to distinguish between librarians and members.
    """
    USER_TYPE_CHOICES = (
        ('librarian', 'Librarian'),
('member', 'Member'),
)
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='member'
    )
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    def is_librarian(self):
        """Helper method to check if user is a librarian"""
        return self.user_type == 'librarian'
    def is_member(self):
        """Helper method to check if user is a member"""
        return self.user_type == 'member'