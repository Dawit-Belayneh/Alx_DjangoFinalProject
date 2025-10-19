<<<<<<< HEAD
# 🛍️ Shop Management API

A **Django REST Framework (DRF)**-based backend system for managing shop operations. This project include full **authentication**, **role-based access control** (Admin & Cashier), and CRUD APIs for  **Products**, **Categories**, **Sales**, **Sale Items**, and **Customers**.

---

## 🚀 Features

**User Roles**

* **Admin:** Full access (Create, Read, Update, Delete)
* **Cashier:** Limited access (Create, Read, Update only)

**Authentication**

* Token-based authentication using DRF's `TokenAuthentication`
* Login and Signup endpoints with role management

**Core APIs**

* **User Management:** Admin-only access
* **Products:** CRUD operations
* **Sales & Items:** Manage transactions
* **Customers:** Maintain customer records

**Buitl With**

* Python 3.x
* Django
* Django REST Framework
* SQLite 

 ---

 ## ⚙️ Installation

 ### 1️⃣ Clone the repository

 ```bash
 git clone https://github.com/Dawit-Belayneh/shop_management.git
 cd shop_management
 ```

 ### 2️⃣ Create and activate a virtual environment

 ```bash
 python -m venv venv
 source venv/bin/activate # On Windows: venv\Scripts\activate
 ```

 ### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py makemigrations main
python manage.py migrate
```

### 5️⃣ Create a superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

The server will start at:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🔑 Authentication Setup

The project uses **Token Authentication**.
Use these steps to test APIs in **Postman**:

1. **Signup (POST)** `/api/signup/`
2. **Login (POST)** `/api/login/` → returns an authentication token
3. Copy the token and add it to request headers:

    ```
    Authorization: Token your_token_here
    ```

---

## 📦 API Endpoints

### Authentication

| Method | Endpoint       | Description                          |
| ------ | -------------- | ------------------------------------ |
| POST   | `/api/signup/` | Register new user (Admin or Cashier) |
| POST   | `/api/login/`  | Login and get authentication token   |

---

### 👥 Users

| Method | Endpoint           | Access | Description    |
| ------ | ------------------ | ------ | -------------- |
| GET    | `/api/users/`      | Admin  | List all users |
| GET    | `/api/users/<id>/` | Admin  | Retrieve user  |
| PATCH  | `/api/users/<id>/` | Admin  | Update user    |
| DELETE | `/api/users/<id>/` | Admin  | Delete user    |

---

### 🏷️ Categories

| Method | Endpoint                | Access          | Description         |
| ------ | ----------------------- | --------------- | ------------------- |
| GET    | `/api/categories/`      | All             | List categories     |
| POST   | `/api/categories/`      | Admin & Cashier | Create new category |
| PATCH  | `/api/categories/<id>/` | Admin & Cashier | Update category     |
| DELETE | `/api/categories/<id>/` | Admin only      | Delete category     |

---

### 🏷️ Categories

| Method | Endpoint                | Access          | Description         |
| ------ | ----------------------- | --------------- | ------------------- |
| GET    | `/api/categories/`      | All             | List categories     |
| POST   | `/api/categories/`      | Admin & Cashier | Create new category |
| PATCH  | `/api/categories/<id>/` | Admin & Cashier | Update category     |
| DELETE | `/api/categories/<id>/` | Admin only      | Delete category     |

---

### 💰 Sales

| Method | Endpoint           | Description    |
| ------ | ------------------ | -------------- |
| GET    | `/api/sales/`      | List all sales |
| POST   | `/api/sales/`      | Create a sale  |
| GET    | `/api/sales/<id>/` | Retrieve sale  |
| PATCH  | `/api/sales/<id>/` | Update sale    |
| DELETE | `/api/sales/<id>/` | Delete sale    |

---

### 🧾 Sale Items

| Method | Endpoint               | Description         |
| ------ | ---------------------- | ------------------- |
| GET    | `/api/saleitems/`      | List all sale items |
| POST   | `/api/saleitems/`      | Create a sale item  |
| GET    | `/api/saleitems/<id>/` | Retrieve sale item  |
| PATCH  | `/api/saleitems/<id>/` | Update sale item    |
| DELETE | `/api/saleitems/<id>/` | Delete sale item    |

---

### 👨‍👩‍👧 Customers

| Method | Endpoint               | Description       |
| ------ | ---------------------- | ----------------- |
| GET    | `/api/customers/`      | List customers    |
| POST   | `/api/customers/`      | Create customer   |
| GET    | `/api/customers/<id>/` | Retrieve customer |
| PATCH  | `/api/customers/<id>/` | Update customer   |
| DELETE | `/api/customers/<id>/` | Delete customer   |

---

## 🔐 Role-Based Access Summary

| Action | Admin | Cashier |
| ------ | ----- | ------- |
| View   | ✅     | ✅       |
| Create | ✅     | ✅       |
| Update | ✅     | ✅       |
| Delete | ✅     | ❌       |

---

## Future Improvements 

* JWT Authentication
* Frontend integration
* Stock managment dashboard
