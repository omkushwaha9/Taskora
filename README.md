
# Taskora — Django Task Management App

Taskora is a task management web application built with **Python and Django**, featuring user authentication, task CRUD operations, form validation, and SQLite database integration.

## Features

- User registration, login, and logout
- Create, view, edit, and delete tasks
- Track pending and completed tasks
- User-specific task management
- Form validation using Django Forms
- Django Admin integration
- SQLite database with Django ORM

## Tech Stack

- **Language:** Python
- **Framework:** Django
- **Database:** SQLite
- **Frontend:** HTML, CSS, Django Templates
- **Tools:** Git, GitHub, VS Code

## Project Structure

```text
Taskora/
├── config/
│   ├── settings.py
│   └── urls.py
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   ├── static/
│   │   └── tasks/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/omkushwaha9/Taskora.git
cd Taskora
```

### 2. Create a Virtual Environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create an Administrator Account

```bash
python manage.py createsuperuser
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open the application at:

- **App:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/
- **Login:** http://127.0.0.1:8000/login/
- **Register:** http://127.0.0.1:8000/register/

## Database Model

Each task contains:

| Field | Description |
|---|---|
| `id` | Unique task identifier |
| `user` | Task owner |
| `title` | Task title |
| `description` | Task description |
| `is_completed` | Completion status |
| `created_at` | Creation timestamp |

## Learning Objectives

- Django project and app architecture
- Models, migrations, and Django ORM
- URL routing and views
- Templates and forms
- Authentication and authorization
- CRUD operations
- SQLite database integration

## Running Tests

```bash
python manage.py test
```

## Future Enhancements

- Task priorities and due dates
- Search, filtering, and pagination
- Dashboard statistics
- Responsive UI
- Automated testing
- Django REST Framework API

## Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/6.1/intro/tutorial01/)
- [Django Models](https://docs.djangoproject.com/en/6.1/topics/db/models/)

## Author

**Om Kushwaha**

- [GitHub](https://github.com/omkushwaha9)
- [LinkedIn](https://www.linkedin.com/in/omkushwaha9/)

## License

This project is intended for educational and portfolio purposes.
