# (1) Connect to MySQL
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",  # change if needed
    password="Akashm@123",  # change to your real password
    database="banking_system"
)

cursor = conn.cursor()

 