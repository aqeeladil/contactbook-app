# Django Mini-Project: Contact Book

## Objective: 
Develop a simple web-based Contact Book using Django. The application must support user login/logout and CRUD operations (Create, Read, Update, Delete) on contact entries. Each user should only be able to access their own contacts.

---

## Suggested Project Structure: 
```
contactbook/ 
├── contactbook/ 
│   ├── settings.py 
│   ├── urls.py 
├── contacts/ 
│   ├── models.py 
│   ├── views.py 
│   ├── urls.py 
│   ├── forms.py 
│   └── templates/ 
|       |── contacts/       
|       |── registration/ 
├── manage.py 
```

---

## Technical Requirements: 
- Use Django's default User model and auth views. 
- Use ModelForm to handle forms. 
- Use @login_required decorator for view protection. 
- Basic HTML templates (no styling needed). 
- Functional structure with clean separation of logic. 

---

## Features Required: 

### 1. Authentication: 
- Login & logout using Django’s built-in auth system. 
- Only logged-in users can manage/view contacts. 
- Unauthorized users should be redirected to the login page. 

### 2. Contact Management (CRUD): 
- Add Contact: Fields — Name, Phone, Email, Address. 
- View Contact List: Show all contacts of the logged-in user. 
- Update Contact: Edit any contact’s info. 
- Delete Contact: Remove a contact. 

### 3. User Data Isolation: 
- Each contact entry is associated with the user who created it. 
- Users should not access other users' contacts. 

### 4. Search: 
- Simple search bar to filter contacts by name or email. 

---

## What to Include: 

### 1. README.md with: 
- Project title and description 
- Setup instructions (how to create venv, migrate DB, run server) 
- How to create a superuser or login 
- Mention any optional features you added 


### 2. .gitignore with: 
```
__pycache__/ 
*.pyc 
db.sqlite3 
.env 
*.log 
*.vscode/ 
.idea/ 
```
