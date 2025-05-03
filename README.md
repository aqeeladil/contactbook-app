# 📒 Contact Book App

A simple and secure web-based Contact Book built with Django. Users can register, log in, and manage their personal contacts (add, view, update, delete). Each user's data is private and isolated.

---

## 🔧 Features

- ✅ User Registration, Login & Logout
- ✅ Create, Read, Update, Delete (CRUD) contacts
- ✅ Contact search by name or email
- ✅ User-specific data access (data isolation)
- ✅ Secure logout via POST
- ✅ Clean and simple HTML templates

---

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

```bash
# Clone the project
git clone https://github.com/aqeeladil/contactbook-app
cd contactbook-app

# Create and activate a virtual environment
python -m venv .venv
source .venv/Scripts/activate  # Windows (git bash)
# Use `source .venv/bin/activate` for Linux/Mac
# Use `.\.venv\Scripts\activate` for Windows CMD

# Install required dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigtrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser   

# Run the server
python manage.py runserver

# Note: If you encounter issues with with migrations or the server, try deleting the migration files and the database file before running the command again.
```

---

## 📚 Render Deployment (Optional) 

```bash
# Build Command:
pip install -r requirements.txt

# Start Command:
gunicorn contactbook.wsgi
```

```

