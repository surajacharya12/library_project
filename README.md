# Library Management System - Authentication Module

## 📚 Project Overview
This is a Django-based Library Management System with a complete authentication module that supports two types of users:
- **Librarians**: Can manage books, members, and dispatch books
- **Members**: Can view available books only

## ✅ Completed Features

### 1. Custom User Model
- Extended Django's `AbstractUser` to include a `user_type` field
- Two user types: `librarian` and `member`
- Helper methods: `is_librarian()` and `is_member()`

### 2. Authentication System
- Login functionality with role-based redirection
- Logout functionality
- Session management
- Password authentication
- CSRF protection

### 3. Admin Interface
- Custom admin interface for user management
- User list with filters (user_type, is_staff, is_active)
- Search functionality (username, email, first_name, last_name)
- Easy user creation and editing

### 4. Role-Based Dashboards
- **Librarian Dashboard**: Access to manage books, members, and dispatch books
- **Member Dashboard**: Limited access to view available books only

### 5. Templates
- Base template with consistent styling
- Login page with form validation
- Librarian dashboard with quick links
- Member dashboard with limited options
- Message system for user feedback

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Django 4.2 or higher
- Virtual environment (venv)

### Installation

1. **Activate Virtual Environment**
   ```bash
   source venv/bin/activate
   ```

2. **Apply Migrations** (Already done)
   ```bash
   python manage.py migrate
   ```

3. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

4. **Access the Application**
   - Main Application: http://127.0.0.1:8000/
   - Admin Interface: http://127.0.0.1:8000/admin/

## 👥 Test Accounts

### Admin (Superuser)
- **Username**: `admin`
- **Password**: `admin123`
- **User Type**: Librarian
- **Permissions**: Full admin access

### Test Librarian
- **Username**: `librarian1`
- **Password**: `librarian123`
- **User Type**: Librarian
- **Name**: John Doe

### Test Member
- **Username**: `member1`
- **Password**: `member123`
- **User Type**: Member
- **Name**: Jane Smith

## 📁 Project Structure

```
library_project/
├── accounts/                      # Authentication app
│   ├── migrations/
│   │   └── 0001_initial.py       # User model migration
│   ├── templates/
│   │   └── accounts/
│   │       ├── base.html         # Base template
│   │       ├── login.html        # Login page
│   │       ├── librarian_dashboard.html
│   │       └── member_dashboard.html
│   ├── admin.py                  # Custom admin configuration
│   ├── models.py                 # Custom User model
│   ├── urls.py                   # URL patterns
│   └── views.py                  # View functions
├── library_system/               # Project settings
│   ├── settings.py               # Django settings
│   └── urls.py                   # Main URL configuration
├── create_superuser.py           # Script to create admin
├── create_test_users.py          # Script to create test users
├── verify_auth.py                # Authentication verification script
├── db.sqlite3                    # SQLite database
└── manage.py                     # Django management script
```

## 🔧 Utility Scripts

### Create Superuser
```bash
python create_superuser.py
```
Creates an admin account with librarian privileges.

### Create Test Users
```bash
python create_test_users.py
```
Creates test accounts for both librarian and member roles.

### Verify Authentication
```bash
python verify_auth.py
```
Runs comprehensive tests to verify the authentication system is working correctly.

## 🎯 How to Test

1. **Start the server**:
   ```bash
   source venv/bin/activate
   python manage.py runserver
   ```

2. **Test Librarian Login**:
   - Go to http://127.0.0.1:8000/
   - Login with `librarian1` / `librarian123`
   - You should see the Librarian Dashboard
   - Click "Logout"

3. **Test Member Login**:
   - Login with `member1` / `member123`
   - You should see the Member Dashboard with limited options
   - Click "Logout"

4. **Test Admin Interface**:
   - Go to http://127.0.0.1:8000/admin/
   - Login with `admin` / `admin123`
   - Navigate to Users to see all accounts
   - Try creating a new user

5. **Test Invalid Login**:
   - Try logging in with incorrect credentials
   - You should see an error message

## 🔐 Security Features

- ✅ Password hashing using Django's built-in system
- ✅ CSRF protection on all forms
- ✅ Login required decorators on protected views
- ✅ Session-based authentication
- ✅ Role-based access control

## 📝 Key Concepts Implemented

1. **Models**: Custom User model extending AbstractUser
2. **Migrations**: Database schema management
3. **Views**: Login, logout, and dashboard views
4. **Templates**: HTML pages with Django template language
5. **URLs**: URL routing and patterns
6. **Authentication**: Django's built-in auth system
7. **Admin**: Custom admin interface
8. **Messages**: User feedback system

## 🎨 Features Breakdown

### Login System
- Username and password authentication
- Role-based redirection after login
- Error messages for invalid credentials
- Success messages for successful login

### Dashboard System
- Separate dashboards for librarians and members
- Role-specific navigation links
- Logout functionality
- Welcome messages with username

### Admin Interface
- User management (create, edit, delete)
- User type filtering
- Search functionality
- Custom fieldsets for user_type

## 🔄 Next Steps (Section 3)

The next section will implement the **Books Management Module** where:
- Librarians can add, edit, view, and delete books
- Books will have fields like title, author, ISBN, quantity, etc.
- Book listing and search functionality
- Book availability tracking

## 📊 Database Schema

### User Model
| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key (auto) |
| username | String | Unique username |
| email | Email | User email address |
| password | String | Hashed password |
| first_name | String | User's first name |
| last_name | String | User's last name |
| user_type | String | 'librarian' or 'member' |
| is_staff | Boolean | Admin access |
| is_active | Boolean | Account status |
| is_superuser | Boolean | Superuser status |
| date_joined | DateTime | Account creation date |
| last_login | DateTime | Last login timestamp |

## 🐛 Troubleshooting

### Issue: "No module named 'django'"
**Solution**: Make sure you've activated the virtual environment:
```bash
source venv/bin/activate
```

### Issue: "Table doesn't exist"
**Solution**: Run migrations:
```bash
python manage.py migrate
```

### Issue: "CSRF verification failed"
**Solution**: Make sure `{% csrf_token %}` is included in all forms.

### Issue: "Page not found (404)"
**Solution**: Check that the URL patterns are correctly configured in `urls.py`.

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Authentication System](https://docs.djangoproject.com/en/4.2/topics/auth/)
- [Django Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [Django Templates](https://docs.djangoproject.com/en/4.2/topics/templates/)

## ✨ Summary

You have successfully completed Section 2 of the Library Management System! 

**What you've built:**
- ✅ Custom User model with user types
- ✅ Database tables using migrations
- ✅ User registration in Django admin
- ✅ Login and logout functionality
- ✅ Role-based dashboards
- ✅ URL routing system
- ✅ HTML templates with styling
- ✅ Complete authentication flow

**Test it out:**
1. Run `python manage.py runserver`
2. Visit http://127.0.0.1:8000/
3. Login with the test accounts
4. Explore the dashboards
5. Test the admin interface

Great job! You're ready to move on to Section 3: Books Management Module! 🎉
# library_project
