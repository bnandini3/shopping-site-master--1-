import sqlite3

conn = sqlite3.connect('data.db')
print("Opened database successfully")

conn.execute('CREATE TABLE items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT NOT NULL, price INTEGER NOT NULL, category TEXT NOT NULL,image TEXT NOT NULL)')
print("Table created successfully")

conn.close()
