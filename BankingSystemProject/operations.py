# (3) Banking Operations
from db_config import conn, cursor

def check_balance(user_id):
    cursor.execute("SELECT balance FROM users WHERE id=%s", (user_id,))
    print("Your balance is: ₹", cursor.fetchone()[0])

def deposit(user_id):
    amount = float(input("Enter amount to deposit: "))
    cursor.execute("UPDATE users SET balance = balance + %s WHERE id=%s", (amount, user_id))
    cursor.execute("INSERT INTO transactions (user_id, type, amount) VALUES (%s, %s, %s)", (user_id, "Deposit", amount))
    conn.commit()
    print("Deposit successful!")

def withdraw(user_id):
    amount = float(input("Enter amount to withdraw: "))
    cursor.execute("SELECT balance FROM users WHERE id=%s", (user_id,))
    balance = cursor.fetchone()[0]
    if amount > balance:
        print("Insufficient balance!")
    else:
        cursor.execute("UPDATE users SET balance = balance - %s WHERE id=%s", (amount, user_id))
        cursor.execute("INSERT INTO transactions (user_id, type, amount) VALUES (%s, %s, %s)", (user_id, "Withdraw", amount))
        conn.commit()
        print("Withdrawal successful!")

def view_transactions(user_id):
    cursor.execute("SELECT type, amount, timestamp FROM transactions WHERE user_id=%s", (user_id,))
    for row in cursor.fetchall():
        print(f"{row[0]} ₹{row[1]} on {row[2]}")
