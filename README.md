# Student Management System (SCMS)

A Django-based student and course management system with enrollment, dashboard, and user account features.

## Project structure

- `student_management/` - Django project settings and root config
- `accounts/` - user account app
- `courses/` - course creation, listing, update, delete pages
- `dashboard/` - dashboard views and templates
- `enrollments/` - enrollment management app
- `students/` - student records and student-related pages
- `media/` - uploaded student images
- `static/` - shared static assets

## Requirements

- Python 3.11+ (or compatible Python 3.x)
- Django 4.x

## Setup

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install django
   ```

3. Run migrations:

   ```bash
   cd student_management
   python manage.py migrate
   ```

4. Create a superuser (optional):

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser:
   ```
   http://127.0.0.1:8000/
   ```

## Notes

- The project already includes `alertify.js` support in `templates/base.html` for Django messages.
- The `.gitignore` file ignores the virtual environment, Python cache files, SQLite database, editor settings, and macOS files.

## Recommended next steps

- Add a `requirements.txt` file with pinned dependencies.
- Add a `.env` file for secret keys and deployment settings if needed.
## photos
![image_alt](https://github.com/SuzanLama433/Student_management_system_scms/blob/5ea76ab7c272dcef11b75e4518d0fc47ec8be28c/p1.png)
![image_alt](https://github.com/SuzanLama433/Student_management_system_scms/blob/5ea76ab7c272dcef11b75e4518d0fc47ec8be28c/p2.png)
![image_alt](https://github.com/SuzanLama433/Student_management_system_scms/blob/5ea76ab7c272dcef11b75e4518d0fc47ec8be28c/p3.png)
![image_alt](https://github.com/SuzanLama433/Student_management_system_scms/blob/5ea76ab7c272dcef11b75e4518d0fc47ec8be28c/p4.png)
