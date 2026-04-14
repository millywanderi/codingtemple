# Flask Users & Pets API 🐾

A simple Flask REST API using MySQL, SQLAlchemy, and Marshmallow.  
It manages users and pets with a many-to-many relationship (users can adopt multiple pets).

---

## 🚀 Features

- Create, read, update, delete users
- Create pets
- Assign pets to users
- Assign multiple pets at once
- View a user’s pets
- MySQL database integration
- ORM using SQLAlchemy 2.0 style
- Data validation using Marshmallow

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- MySQL
- SQLAlchemy ORM

---

## 📦 Installation

### 1. Clone the project
    git clone <restful_apis>
    cd <restful_apis>

### 2. Create a virtual environment
    python3 -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows

### 3. Install dependencies
    pip install -r requirements.txt

---

## 🗄️ Database Setup (MySQL)

Create the database:

    CREATE DATABASE flask_api_db;

Update your database credentials in the app:

    mysql+mysqlconnector://username:password@localhost/flask_api_db

---

## ▶️ Run the App

    python app.py

Server runs at:

    http://127.0.0.1:5000

---

## 📌 API Endpoints

### Users
- POST /users → Create user  
- GET /users → Get all users  
- GET /users/<id> → Get user by ID  
- PUT /users/<id> → Update user  
- DELETE /users/<id> → Delete user  

### Pets
- POST /pets/ → Create pet  

### Relationships
- GET /users/<user_id>/add_pet/<pet_id>/ → Add single pet to user  
- POST /users/<user_id>/add_pets → Add multiple pets to user  
- GET /users/my_pets/<user_id> → View user's pets  

---

## 🧪 Example JSON

### Create User
    {
      "name": "John Doe",
      "email": "john@example.com"
    }

### Create Pet
    {
      "name": "Buddy",
      "animal": "Dog"
    }

### Add Multiple Pets
    {
      "pet_ids": [1, 2, 3]
    }

---

## ⚠️ Notes

- Make sure MySQL is running before starting the app
- Tables are auto-created using db.create_all()
- Debug mode is enabled by default

---

## 📄 requirements.txt

Flask
Flask-SQLAlchemy
Flask-Marshmallow
marshmallow
SQLAlchemy
mysql-connector-python
