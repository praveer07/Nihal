import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Connect to MySQL database
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = db.cursor()

# Create a table
def create_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)
    db.commit()

# Insert data
def create_employee(name, email):
    insert_query = "INSERT INTO employees (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(insert_query, values)
    db.commit()

# Read data
def read_employee(employee_id):
    select_query = "SELECT * FROM employees WHERE id = %s"
    cursor.execute(select_query, (employee_id,))
    employee = cursor.fetchone()
    if employee:
        print("Employee ID:", employee[0])
        print("Name:", employee[1])
        print("Email:", employee[2])
    else:
        print("Employee not found")

# Update data
def update_employee(employee_id, new_name, new_email):
    update_query = "UPDATE employees SET name = %s, email = %s WHERE id = %s"
    values = (new_name, new_email, employee_id)
    cursor.execute(update_query, values)
    db.commit()

# Delete data
def delete_employee(employee_id):
    delete_query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(delete_query, (employee_id,))
    db.commit()

if __name__ == "__main__":
    create_table()
    
    # Create an employee
    create_employee("Praveer", "johndoe@email.com")
    
    # Read employee data
    read_employee(1)
    
    # Update employee data
    update_employee(1, "John Smith", "johnsmith@email.com")
    
    # Read updated employee data
    read_employee(1)
    
    # Delete employee
    delete_employee(1)
    
    # Confirm deletion
    read_employee(1)
    
    db.close()

