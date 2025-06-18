# (2) Signup / Login System
from db_config import conn, cursor

def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    print("Signup successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    if result:
        print("Login successful!")
        return result[0]  # return user_id
    else:
        print("Invalid credentials.")
        return None
