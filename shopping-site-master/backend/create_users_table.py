import sqlite3

conn = sqlite3.connect('data.db')
print("Opened database successfully")

conn.execute('CREATE TABLE users (username TEXT, password TEXT)')
print("Table created successfully")

conn.close()
