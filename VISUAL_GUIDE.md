# 📸 Visual Guide - What You'll See

## Application Flow

### 1. Root URL (/)
**What happens**: Automatically redirects to login page
**URL**: http://127.0.0.1:8000/ → http://127.0.0.1:8000/accounts/login/

---

### 2. Login Page
**URL**: http://127.0.0.1:8000/accounts/login/

**What you'll see**:
- Clean white container with blue header
- "Library Management System" title
- Login form with:
  - Username field
  - Password field
  - Blue "Login" button
- Any error/success messages appear above the form

**Try it**:
- Enter: `librarian1` / `librarian123`
- Click "Login"

---

### 3. Librarian Dashboard
**URL**: http://127.0.0.1:8000/accounts/librarian/dashboard/

**What you'll see**:
- Header: "Library Management System"
- Success message: "Welcome back, librarian1!"
- Page title: "Librarian Dashboard"
- Red "Logout" link in top-right
- Welcome text: "Welcome, librarian1! You are logged in as a librarian."
- Quick Links section with:
  - Manage Books (placeholder link)
  - Manage Members (placeholder link)
  - Dispatch Books (placeholder link)

**Features**:
- Full access to library management
- Quick navigation to all features
- Logout option

---

### 4. Member Dashboard
**URL**: http://127.0.0.1:8000/accounts/member/dashboard/

**What you'll see**:
- Header: "Library Management System"
- Success message: "Welcome back, member1!"
- Page title: "Member Dashboard"
- Red "Logout" link in top-right
- Welcome text: "Welcome, member1! You are logged in as a member."
- Available Options section with:
  - View Available Books (placeholder link)

**Features**:
- Limited access (view only)
- Single navigation option
- Logout option

---

### 5. Logout Flow
**What happens**:
1. Click "Logout" link
2. Session is cleared
3. Redirect to login page
4. Info message: "You have been logged out successfully."

---

### 6. Admin Interface
**URL**: http://127.0.0.1:8000/admin/

**What you'll see**:
- Django admin login page (if not logged in)
- After login with `admin` / `admin123`:
  - Django admin dashboard
  - "Accounts" section with "Users" link
  - Click "Users" to see all user accounts

**User List Features**:
- Columns: Username, Email, User Type, Staff Status, Active Status
- Filters: User Type, Staff Status, Active Status
- Search: Username, Email, First Name, Last Name
- Actions: Add user, Edit user, Delete user

**Adding a New User**:
1. Click "Add User +"
2. Fill in username and password
3. Click "Save and continue editing"
4. Set user_type (librarian or member)
5. Fill in additional details
6. Click "Save"

---

## Message System

### Success Messages (Green)
- "Welcome back, [username]!"
- Displayed after successful login

### Error Messages (Red)
- "Invalid username or password."
- Displayed when login fails

### Info Messages (Blue)
- "You have been logged out successfully."
- Displayed after logout

---

## Color Scheme

- **Primary Blue**: #3498db (buttons, links, header border)
- **Dark Blue**: #2c3e50 (headings)
- **Hover Blue**: #2980b9 (button hover)
- **Red**: #e74c3c (logout link)
- **Background**: #f4f4f4 (page background)
- **White**: #ffffff (container background)

---

## Responsive Design

The application uses a responsive container:
- Max width: 1200px
- Centered on page
- White background with shadow
- Padding: 30px
- Border radius: 8px

---

## Testing Checklist

### ✅ Test 1: Root Redirect
1. Go to http://127.0.0.1:8000/
2. Should redirect to login page

### ✅ Test 2: Librarian Login
1. Login with `librarian1` / `librarian123`
2. Should see Librarian Dashboard
3. Should see success message
4. Should see 3 quick links

### ✅ Test 3: Logout
1. Click "Logout"
2. Should redirect to login
3. Should see logout message

### ✅ Test 4: Member Login
1. Login with `member1` / `member123`
2. Should see Member Dashboard
3. Should see only 1 option

### ✅ Test 5: Invalid Login
1. Try wrong password
2. Should see error message
3. Should stay on login page

### ✅ Test 6: Admin Access
1. Go to /admin/
2. Login with `admin` / `admin123`
3. Should see admin dashboard
4. Click "Users"
5. Should see all 3 users

### ✅ Test 7: Protected Routes
1. Logout completely
2. Try to access /accounts/librarian/dashboard/
3. Should redirect to login page

---

## Browser Testing Tips

### Using Chrome/Firefox DevTools
1. Open DevTools (F12)
2. Go to "Application" tab
3. Check "Cookies" to see session data
4. Check "Storage" to see session info

### Testing Different Roles
1. Open two different browsers (Chrome + Firefox)
2. Login as librarian in one
3. Login as member in other
4. Compare the dashboards

### Testing Session Persistence
1. Login as librarian
2. Close browser tab
3. Open new tab to same URL
4. Should still be logged in

---

## Common Issues & Solutions

### Issue: Can't see login page
**Check**: Is the server running?
```bash
python manage.py runserver
```

### Issue: Login doesn't work
**Check**: Are you using the correct credentials?
- librarian1 / librarian123
- member1 / member123

### Issue: No styling appears
**Check**: Is the CSS in the base.html template?
**Solution**: The CSS is inline in the templates

### Issue: CSRF error on login
**Check**: Is `{% csrf_token %}` in the form?
**Solution**: Already included in login.html

---

## Next Steps

Once you've tested all the features above, you're ready for **Section 3: Books Management Module**!

The next section will add:
- Book listing page
- Add book form (librarians only)
- Edit book form (librarians only)
- Delete book functionality (librarians only)
- View books page (all users)
- Search and filter books

---

**Happy Testing! 🎉**
