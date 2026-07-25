import json
import os
import secrets
import uuid

# Load users from file
if os.path.exists("users.json"):
    with open("users.json", "r") as file:
        users = json.load(file)
else:
    users = {}

employees = []


def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


def signup():
    email = input("Enter Email: ")

    if '@' not in email or '.com' not in email:
        print("Invalid Email!")
        return

    if email in users:
        print("Email already exists. Please Login.")
        return

    password = input("Enter Password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters.")
        return

    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if upper and lower and digit and special:
        users[email] = password
        save_users()
        print("Signup Successful")
    else:
        print("Password must contain Uppercase, Lowercase, Number and Special Character")


def login():

    while True:
        email = input("Enter Email: ")

        if email in users:
            break
        else:
            print("Invalid Email! Try Again.")

    while True:
        password = input("Enter Password: ")

        if users[email] == password:
            print("Login Successful!")
            url_token = secrets.token_urlsafe(32)
            print("Token:", url_token)
            dashboard()
            break
        else:
            print("Incorrect Password! Try Again.")


def generate_uuid():
    return str(uuid.uuid4())


def add_employee():

    auto_id = generate_uuid()
    print("Auto ID:", auto_id)

    id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")
    salary = input("Salary: ")
    hire_date = input("Hire Date: ")

    employees.append({
        "auto_id": auto_id,
        "id": id,
        "name": name,
        "department": department,
        "salary": salary,
        "hire_date": hire_date
    })

    print("Employee Added Successfully")


def view_employee():

    if len(employees) == 0:
        print("No Employees Found")
    else:
        for emp in employees:
            print("--------------------------------")
            for key, value in emp.items():
                print(f"{key}: {value}")


def search_employee():

    dept = input("Enter Department: ")
    salary = int(input("Enter Minimum Salary: "))

    found = False

    for emp in employees:

        if emp["department"].lower() == dept.lower() and int(emp["salary"]) >= salary:
            print("--------------------------------")
            for key, value in emp.items():
                print(f"{key}: {value}")
            found = True

    if not found:
        print("Employee Not Found")


def update_employee():

    emp_id = input("Enter Employee ID: ")

    for emp in employees:

        if emp["id"] == emp_id:
            emp["name"] = input("New Name: ")
            emp["department"] = input("New Department: ")
            emp["salary"] = input("New Salary: ")
            emp["hire_date"] = input("New Hire Date: ")

            print("Employee Updated Successfully")
            return

    print("Employee Not Found")


def delete_employee():

    emp_id = input("Enter Employee ID: ")

    for emp in employees:

        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee Deleted Successfully")
            return

    print("Employee Not Found")


def dashboard():

    while True:

        print("\n========== EMPLOYEE DASHBOARD ==========")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Logout")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employee()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("Logout Successfully")
            break

        else:
            print("Invalid Choice")


while True:

    print("\n========== MAIN MENU ==========")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        signup()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")