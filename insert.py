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


# Insert data
def create_employee(name, email):
    insert_query = "INSERT INTO employees (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(insert_query, values)
    db.commit()
if __name__ == "__main__":
    
    # Create an employee
    create_employee("Praveer", "johndoe@email.com")
    
    
    
    db.close()

