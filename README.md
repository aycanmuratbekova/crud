# Django REST API Project

This is a simple Django REST API project that provides CRUD functionality for managing various resources.

## Features

- CRUD operations for
- API documentation using Swagger
- WebSocket notifications

## Requirements

- Python 3.10
- Django 4.x or 5.x
- Django REST Framework
- Other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/aycanmuratbekova/crud.git
    cd core
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (optional, for accessing the Django admin):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

- **User Profiles**: `/api/user-profiles/`
- **Categories**: `/api/categories/`
- **Products**: `/api/products/`
- **Orders**: `/api/orders/`
- **Reviews**: `/api/reviews/`

Refer to the Swagger documentation for detailed API documentation and usage.

## API Documentation

API documentation is automatically generated using Swagger. Once the server is running, you can access the documentation at: https://devcodecademy.pythonanywhere.com/swagger/


