from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Praveer@2000",
    database="NIHAL"
)
cursor = db.cursor()

# Read all employees
def read_employees():
    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)
    employees = cursor.fetchall()
    return employees

@app.route('/employees')
def display_employees():
    employees = read_employees()
    return render_template('employees.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
