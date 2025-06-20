# (2) Signup / Login System
from db_config import conn, cursor

from db_config import conn, cursor

def signup():
    print("\n--- Signup ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # New: Ask for security question and answer
    security_question = input("Enter a security question (e.g. What is your pet's name?): ")
    security_answer = input("Enter answer to your security question: ")

    try:
        cursor.execute("""
            INSERT INTO users (username, password, security_question, security_answer)
            VALUES (%s, %s, %s, %s)
        """, (username, password, security_question, security_answer))
        conn.commit()
        print("Signup successful!\n")
    except Exception as e:
        print("Error during signup:", e)


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

def forgot_password():
    print("\n--- Forgot Password ---")
    username = input("Enter your username: ")

    cursor.execute("SELECT security_question, security_answer FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        question, correct_answer = result

        # ✅ Handle missing security question/answer
        if not question or not correct_answer:
            print("❌ This user has no security question set. Please contact admin or create a new account.\n")
            return

        print("Security Question:", question)
        answer = input("Enter your answer: ")

        if answer.strip().lower() == correct_answer.strip().lower():
            new_password = input("Enter new password: ")
            cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
            conn.commit()
            print("✅ Password reset successful!\n")
        else:
            print("❌ Incorrect answer. Password reset failed.\n")
    else:
        print("❌ Username not found.\n")
