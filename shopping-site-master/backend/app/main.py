import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return 'Hello World'


@app.route('/items/category/<string:category>')
def get_items_by_category(category):
    con = sqlite3.connect('data.db')
    cur = con.cursor()

    if category == 'all':
        query = cur.execute('SELECT * FROM items')
    else:
        query = cur.execute(
            'SELECT * FROM items WHERE category=?', (category,))
    rows = query.fetchall()
    column_names = [description[0] for description in query.description]
    items = [dict(zip(column_names, row)) for row in rows]

    con.close()

    return jsonify({'items': items})


@app.route('/signup', methods=['POST'])
def signup():
    # Retrieve the username and password from the request body
    username = request.json.get('username')
    password = request.json.get('password')

    # Validate that the username and password are not empty
    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    # Open a connection to the database
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    try:
        # Check if the username already exists in the database
        query = cur.execute(
            'SELECT * FROM users WHERE username = ?', (username,))
        existing_user = query.fetchone()
        if existing_user:
            return jsonify({'message': 'Username already exists.'}), 400

        # Insert the new user into the database
        cur.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()

        return jsonify({'message': 'User created successfully.'}), 201
    except Exception as e:
        print(e)
        return jsonify({'message': 'Something went wrong.'}), 500
    finally:
        conn.close()


@app.route('/login', methods=['POST'])
def login():
    # Retrieve the username and password from the request body
    username = request.json.get('username')
    password = request.json.get('password')

    # Validate that the username and password are not empty
    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    # Open a connection to the database
    print("Opening database connection")
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    try:
        # Retrieve the user with the given username from the database
        query = cur.execute(
            'SELECT * FROM users WHERE username = ?', (username,))
        user = query.fetchone()

        # Validate that the user exists and that the password is correct
        if not user or not user[1] == password:
            return jsonify({'message': 'Invalid credentials.'}), 401

        return jsonify({'message': 'Login successful.'}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'Something went wrong.'}), 500
    finally:
        print("Closing database connection")
        conn.close()
