# (4) Main Menu and Application Entry Point
from auth import *
from operations import check_balance, deposit, withdraw, view_transactions


def main():
    print("Welcome to the Banking System")
    while True:
        print("1. Signup")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            signup()
        elif choice == "2":
            user_id = login()
            if user_id:
                while True:
                    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. View Transactions\n5. Logout")
                    ch = input("Choose: ")
                    if ch == "1":
                        check_balance(user_id)
                    elif ch == "2":
                        deposit(user_id)
                    elif ch == "3":
                        withdraw(user_id)
                    elif ch == "4":
                        view_transactions(user_id)
                    elif ch == "5":
                        break
                    else:
                        print("Invalid option.")
        elif choice == '3':
            forgot_password()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
main()
