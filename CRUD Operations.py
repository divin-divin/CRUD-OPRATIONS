#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')
get_ipython().system('pip install ipywidgets')


# In[2]:


import mysql.connector
from mysql.connector import Error


# In[15]:


# Function to connect to the MySQL Database
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # MySQL Host
            user='root',       # MySQL Username
            password='root',  # MySQL Password
            database='crud_opration'  # Database name
        )
        if connection.is_connected():
            print("Connected to MySQL Database")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

# Function to handle the login process
def login(username, password):
    if username == "WTT" and password == "WTT":  # Simple hardcoded admin login
        print("Login successful!")
        operations()
    else:
        print("Invalid username,password. Please try again.")

# CRUD Operations Menu
def operations():
    while True:
        print("Select the below menu:")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        
        operation = input("Select an operation (1-5): ")
        
        if operation == '1':
            create_user()
        elif operation == '2':
            read_users()
        elif operation == '3':
            update_user()
        elif operation == '4':
            delete_user()
        elif operation == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Create User
def create_user():
    name = input("Enter name: ")
    email_id = input("Enter email: ")
    ph_num = input("Enter phone number: ")
    age = int(input("Enter age: "))
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO user_details (name, email_id, ph_num, age) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (name, email_id, ph_num, age))
            connection.commit()
            print("User created successfully.")
        except Error as e:
            print(f"Error: {e}")
        cursor.close()
        connection.close()

# Read Users
def read_users():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM user_details"
        cursor.execute(query)
        records = cursor.fetchall()
        print("\nUsers in the database:")
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}, Email: {record[2]}, Phone: {record[3]}, Age: {record[4]}")
        cursor.close()
        connection.close()

# Update User
def update_user():
    user_id = int(input("Enter user ID to update: "))
    name = input("Enter new name: ")
    email_id = input("Enter new email: ")
    ph_num = input("Enter new phone number: ")
    age = int(input("Enter new age: "))
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE user_details SET name = %s, email_id = %s, ph_num = %s, age = %s WHERE id = %s"
        cursor.execute(query, (name, email_id, ph_num, age, user_id))
        connection.commit()
        print("User updated successfully.")
        cursor.close()
        connection.close()

# Delete User
def delete_user():
    user_id = int(input("Enter user ID to delete: "))
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM user_details WHERE id = %s"
        cursor.execute(query, (user_id,))
        connection.commit()
        print("User deleted successfully.")
        cursor.close()
        connection.close()

# Function to start the login interface
def login_interface():
    print("Welcome to WTT International")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login(username, password)

# Start the login interface
login_interface()


# In[ ]:




