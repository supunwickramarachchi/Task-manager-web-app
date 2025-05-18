# ✅ Django Task Manager App

A beautifully designed full-featured **Task Management System** built with **Django**, **Tailwind CSS**, and **PostgreSQL**. This project demonstrates core web development principles, database design, and user experience — all in a clean and production-like structure.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Sign up, login, logout
  - Session-based access control

- 📝 **Task Management**
  - Create, read, update, delete (CRUD) tasks
  - Set title, description, priority, due date, completion status

- 📆 **Due Dates & Priority**
  - Input due date using a clean date picker
  - Select task priority from dropdown
  - Option to mark task as completed

- 🎨 **Clean UI with TailwindCSS**
  - Responsive and mobile-friendly design
  - Tailwind used for all form and page styling

- 🗃️ **Database: PostgreSQL**
  - PostgreSQL used for production-grade relational database
  - Models mapped using Django ORM

- 🛡️ **Security & Best Practices**
  - `.env` file used for sensitive settings
  - `.gitignore` and `requirements.txt` included

---

## 🛠️ Technologies Used

| Category          | Tech Stack |
|-------------------|------------|
| 🧠 Backend         | Django 4+ |
| 🎨 Frontend        | Tailwind CSS |
| 🗃️ Database        | PostgreSQL |
| ⚙️ Deployment Ready| `.env`, `requirements.txt`, clean structure |
| 🧪 Testing         | Manual form testing (unit tests planned) |

---

## 📚 What I Learned From This Project

This project helped me:

- Understand **real-world Django app structure**
- Work with **PostgreSQL** using Django ORM
- Handle form validation and display errors in Django
- Build **clean and responsive** interfaces with TailwindCSS
- Manage task states using checkboxes and priority options
- Implement reusable **templates and views**
- Separate secret configuration using environment variables
- Handle and analyze HTTP logs and requests
- Deploy-ready Django configurations

This was not just a coding task, but a simulation of **real developer workflow** including:

> Problem-solving → Building features → Debugging → Refactoring → Preparing for production → Version control with Git

---

## 📁 Project Structure

```plaintext
taskmanager/
├── tasks/         # Task management app (models, views, forms)
├── users/         # User management app (registration, login, logout)
├── taskmanager/   # Main Django project settings
├── templates/     # Base and shared templates
├── static/        # Optional: Static files for Tailwind (if configured)
├── .env           # Secrets and database config (not tracked in Git)
├── requirements.txt
├── Pipfile
├── Pipfile.lock
├── manage.py
├── LICENSE
└── README.md
```

## 💡 How to Run It

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/task-manager-django.git
cd task-manager-django

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create `.env` file
# Add your Django secret key and database credentials here

# 5. Apply migrations
python manage.py migrate

# 6. Run the server
python manage.py runserver
```

## ✨ Future Improvements
 - Add task filtering (by priority/completion)

 - Search bar for tasks

 - Task deadlines with alerts

 - REST API with Django REST Framework

 - Unit tests for models and views

 - Deployment on Render or Railway

 - Pagination and advanced sorting

## 🤝 Author
_**Supun Wickramarachchi**_
A self-taught developer focused on becoming a skilled Python Software Engineer, with goals of entering the space, robotics, and aerospace software industry.

* Passionate about building smart systems, learning by doing, and pushing the limits with technology.
---
## 📌 License
This project is open-source and free to use under the [MIT License](LICENSE).

_**#django #python #tailwindcss #postgresql #webdevelopment #fullstack #selftaught #portfolio**_