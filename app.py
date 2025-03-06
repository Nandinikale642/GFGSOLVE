from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS
from flask import send_from_directory
import os
from flask_cors import CORS
import mysql.connector

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure MySQL connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # Your MySQL username
        password='N@ndinics109',  # Your MySQL password
        database='m1'  # Your MySQL database
    )
    return connection

@app.route('/')
def home():
     return send_from_directory(os.getcwd(), 'enigma.html') # Render the enigma.html file from the templates folder

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')

    if full_name and email and password:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()

        if user:
            return jsonify({'message': 'User already exists!'}), 400

        cursor.execute('INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)', 
                       (full_name, email, password))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({'message': 'Registration successful! Please log in.'}), 200
    
    return jsonify({'message': 'Please provide all the required details!'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email and password:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        user = cursor.fetchone()

        if user:
            return jsonify({'message': 'Login successful!'}), 200
        else:
            return jsonify({'message': 'Invalid email or password!'}), 400

        cursor.close()
        connection.close()

    return jsonify({'message': 'Please provide both email and password!'}), 400

if __name__=="__main__":
    app.run(port=8000, debug=True) 