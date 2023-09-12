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

# Update data
def update_employee(employee_id, new_name, new_email):
    update_query = "UPDATE employees SET name = %s, email = %s WHERE id = %s"
    values = (new_name, new_email, employee_id)
    cursor.execute(update_query, values)
    db.commit()


if __name__ == "__main__":
    
    
    
    # Update employee data
    update_employee(2, "John Smith", "johnsmith@email.com")
    
    
    
    db.close()