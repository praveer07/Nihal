# app.py

from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Configure your MySQL database connection
db = pymysql.connect(
    host='your_mysql_host',
    user='your_mysql_user',
    password='your_mysql_password',
    db='your_mysql_database',
    cursorclass=pymysql.cursors.DictCursor  # This sets the cursor to return results as dictionaries
)

# API endpoint to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        if 'username' in data and 'email' in data:
            cursor = db.cursor()
            cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)",
                           (data['username'], data['email']))
            db.commit()
            cursor.close()
            return jsonify({"message": "User created successfully"}), 201
        else:
            return jsonify({"error": "Missing 'username' or 'email' in the request body"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all users
@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()

        user_list = []
        for user in users:
            user_dict = {
                'id': user['id'],
                'username': user['username'],
                'email': user['email']
            }
            user_list.append(user_dict)

        return jsonify(user_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
