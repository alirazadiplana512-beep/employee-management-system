# employee-management-system

## Overview

The **Employee Management System** is a command-line application developed in **Python** to manage employee records efficiently. The project provides a secure authentication system with user signup and login, followed by a dashboard where authenticated users can perform employee management operations.

The application demonstrates the practical use of Python programming concepts such as functions, loops, conditional statements, dictionaries, lists, file handling, JSON, UUID generation, and secure token creation.

---

# Features

## User Authentication

* User Signup with email validation.
* Password strength validation.
* User Login with credential verification.
* User data stored permanently in a JSON file.
* Secure session token generated after successful login using Python's `secrets` module.

---

## Employee Management

After logging in, users can:

* Add a new employee.
* View all employees.
* Search employees by department and minimum salary.
* Update employee information.
* Delete employee records.
* Logout from the dashboard.

---

# Technologies Used

* Python 3
* JSON File Handling
* UUID Module
* Secrets Module
* OS Module

---

# Modules Used

### `json`

Used to save and load user information from a JSON file.

### `os`

Checks whether the user database (`users.json`) already exists.

### `uuid`

Generates a unique Auto ID for every employee.

### `secrets`

Creates a secure random login token after successful authentication.

---

# Project Workflow

1. The program starts with the Main Menu.
2. Users can create a new account through Signup.
3. Email and password are validated.
4. User information is stored in `users.json`.
5. Existing users can log in.
6. A secure authentication token is generated.
7. The Employee Dashboard is displayed.
8. Users can perform CRUD operations:

   * Create
   * Read
   * Update
   * Delete
9. Users can logout or exit the application.

---

# Password Validation Rules

The password must contain:

* Minimum 8 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one digit
* At least one special character

---

# Employee Information

Each employee record contains:

* Auto Generated UUID
* Employee ID
* Employee Name
* Department
* Salary
* Hire Date

---

# Learning Outcomes

This project demonstrates the following Python concepts:

* Functions
* Loops
* Conditional Statements
* Dictionaries
* Lists
* JSON File Handling
* File Operations
* Exception-Free Data Validation
* UUID Generation
* Secure Token Generation
* CRUD Operations
* User Authentication

---

# Future Improvements

Possible enhancements include:

* Password hashing for improved security.
* Employee data storage in a database (MySQL or SQLite).
* Login attempt limitation.
* Password recovery feature.
* Admin and User roles.
* Search by Employee ID or Name.
* Export employee records to CSV or Excel.
* Graphical User Interface (GUI) using Tkinter or PyQt.
* Web version using Flask or Django.

---

# Author

**Ali Raza**

BS Cyber Security Student

Python Developer | Learning Cyber Security | GitHub Portfolio Builder
