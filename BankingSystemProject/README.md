# 🏦 Banking Login System in Python

A simple Command-Line Banking System built with **Python** and **MySQL**.  
It allows users to **sign up**, **log in**, and perform banking operations such as checking balance, depositing, withdrawing, and viewing transaction history.

---

## 🚀 Features

- ✅ User Signup and Login
- 💰 Balance Check
- ➕ Deposit Money
- ➖ Withdraw Money
- 📜 Transaction History
- 🔐 Password-based authentication
- 🛢️ MySQL backend for storing user data and transactions

---

## 🧰 Tech Stack

| Technology | Description                |
|------------|----------------------------|
| Python     | Programming language       |
| MySQL      | Relational Database         |
| mysql-connector-python | MySQL-Python integration |

---

## 📁 Project Structure

BankingSystemProject/
├── main.py # Entry point
├── auth.py # Handles signup & login
├── operations.py # Banking operations
├── db_config.py # MySQL connection config
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/akashmadasu/banking-login-system.git
cd banking-login-system

#2. Install Required Python Package
pip install mysql-connector-python


#3. Set Up MySQL Database
Open MySQL Workbench or terminal, and run:

CREATE DATABASE banking_system;
USE banking_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    balance DECIMAL(10,2) DEFAULT 0.00
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    type VARCHAR(20),
    amount DECIMAL(10,2),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);



#4. Configure Database in db_config.py
Update with your MySQL credentials:

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="banking_system"
)


#5. Run the Application

python main.py

🖥️ Example Output (CLI Screenshot)
text
Copy
Edit
Welcome to the Banking System
1.Signup  2.Login  3.Exit
Choose: 1
Enter username: akash
Enter password: ******
Signup successful!

1.Signup  2.Login  3.Exit
Choose: 2
Enter username: akash
Enter password: ******
Login successful!

1. Check Balance
2. Deposit
3. Withdraw
4. View Transactions
5. Logout
Choose: 1
Your current balance is: 0.00


#✍️ Author
Akash Madasu
📧 akash874426@gmail.com
🔗 LinkedIn :- https://www.linkedin.com/in/akashmadasu/
🔗 GitHub :- https://github.com/Akashmadasu1


#📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
---

### ✅ Bonus: `LICENSE` File (MIT License)

You can create a file named `LICENSE` in your repo with this content:

```text
MIT License

Copyright (c) 2025 Akash Madasu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[... full MIT license text continues ...]