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


def delete_employee(employee_id):
    delete_query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(delete_query, (employee_id,))
    db.commit()

if __name__ == "__main__":
    
    
    # Delete employee
    delete_employee(11)
    
    
    
    db.close()

