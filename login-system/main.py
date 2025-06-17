from db_config import get_connection

def sign_up():
    conn = get_connection()
    cursor = conn.cursor()

    username = input("Enter a username: ")
    password = input("Enter a password: ")

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("✅ User registered successfully!")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        conn.close()

def login():
    conn = get_connection()
    cursor = conn.cursor()

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()

    if result:
        print(f"✅ Welcome back, {username}!")
    else:
        print("❌ Invalid username or password.")

    conn.close()

def menu():
    while True:
        print("\n1. Sign Up\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            login()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    menu()
