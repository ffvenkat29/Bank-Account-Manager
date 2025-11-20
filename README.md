Bank Account Manager (Python)

This project is a simple Bank Account Manager implemented using Python classes.
It demonstrates core Object-Oriented Programming (OOP) concepts such as objects, attributes, and methods.
Features
Account Class
  Each account object contains:
  Account Number
  Account Holder Name
  Account Balance
Deposit Function
  Adds money to the account
  Works only when the amount is greater than zero
Withdrawal Function
  Withdraws money only if the withdrawal amount is greater than ₹500
  Updates the balance after successful withdrawal
  Prevents withdrawal of small amounts
Demonstration Code
  Includes example usage:
  Creating an account
  Performing deposit
Bank Account Manager_git.py
      example used in this code :
      
      acc_1 = account(1234566789, "gopi", 500000)
      print(acc_1.acc_name)
      print(acc_1.acc_bal)
      
      acc_1.deposit(5000)
      print(acc_1.acc_bal)
      
      acc_1.withdraw(400)
      print(acc_1.acc_bal)
      Performing withdrawals

Technologies Used:
    -  Python 3.x
    -  Object-Oriented Programming principles

future Enhancements:
  You can extend this project by adding:
      
      PIN authentication system
      
      Transaction history
      
      Account details update
      
      Multiple accounts handling
      
      Menu-driven ATM interface
