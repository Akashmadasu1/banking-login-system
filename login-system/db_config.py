import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Akashm@123",  # ← Replace this with your MySQL password
        database="login_system"
    )
