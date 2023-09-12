import mysql.connector

import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = db.cursor()



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


read_employee(9)