# To-Do List Application

A simple To-Do List application built with Django. This project allows users to manage tasks by adding, updating, and deleting them. It features a basic user interface to interact with the to-do list and manage tasks.

## Features

- Add New Tasks: Users can add new tasks to the list.
- Update Existing Tasks: Users can edit the title of existing tasks and mark them as completed.
- Delete Tasks: Users can remove tasks from the list.
- Mark as Completed: Users can mark tasks as completed with a checkbox.

## Requirements

- Python 3.x
- Django 5.x

## Installation

1. Clone the Repository

   ```bash
   git clone <repository_url>

Replace <repository_url> with the URL of your GitHub repository.

 2. Navigate to the Project Directory

cd todoproject


 3. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


 4. Install Dependencies

pip install -r requirements.txt


 5. Apply Migrations

python manage.py migrate


 6. Run the Development Server

python manage.py runserver

Access the application at http://127.0.0.1:8000/.

Usage

 • Adding a Task: Enter a task title in the input field and click “Add”.
 • Updating a Task: Edit the task title and click “Update” to save changes. Use the checkbox to mark the task as completed.
 • Deleting a Task: Click “Delete” to remove a task from the list.

Project Structure

 • todo/
 • migrations/ - Database migrations.
 • static/ - Static files like CSS.
 • templates/ - HTML templates.
 • init.py - Initialization file for the app.
 • admin.py - Configuration for the Django admin interface.
 • apps.py - Application configuration.
 • models.py - Database models.
 • tests.py - Application tests.
 • urls.py - URL patterns for the app.
 • views.py - View functions for handling requests.
 • todoproject/ - Project directory.
 • init.py - Initialization file for the project.
 • settings.py - Project settings.
 • urls.py - URL patterns for the project.
 • wsgi.py - WSGI configuration for deploying the project.
 • manage.py - Command-line utility for Django projects.

Contributing

If you’d like to contribute to this project, please fork the repository and submit a pull request with your changes.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements

 • Django documentation for guidance on creating web applications.
 • GitHub for hosting the project.
