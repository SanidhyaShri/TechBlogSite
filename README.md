# TechBlogSite

A full-stack blogging web application built using **Python**, **Django**, **MySQL**, and **Bootstrap**. The platform allows users to create, manage, and interact with blog posts through a clean and responsive interface.

---

## Features

- User Registration and Login
- Secure Authentication and Authorization
- Create, Read, Update, and Delete (CRUD) Blog Posts
- Like and Unlike Posts
- Comment on Blog Posts
- Responsive User Interface using Bootstrap
- MySQL Database Integration with Django ORM
- User-specific Post Management

---

## Tech Stack

**Backend**
- Python
- Django

**Frontend**
- HTML5
- CSS3
- Bootstrap 5

**Database**
- MySQL
- Django ORM

**Tools**
- Git
- GitHub
- VS Code

---

## Project Structure

```
TechBlogSite/
│
├── posts/
├── techblogsite/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/SanidhyaShri/TechBlogSite.git
```

### Navigate to the Project

```bash
cd TechBlogSite
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Update the database settings in `settings.py` with your MySQL credentials.

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---


## Future Enhancements

- Search Functionality
- User Profile Page
- Categories and Tags
- Rich Text Editor
- Image Uploads
- Email Notifications
- Pagination
- Dark Mode

---

## Author

**Sanidhya Shrivastava**

GitHub:
https://github.com/SanidhyaShri

---

## License

This project is created for learning purposes and personal portfolio use.
