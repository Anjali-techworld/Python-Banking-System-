# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:54:49 2024

@author: ANJALI L
"""

class BankAccount:
    def __init__(self, account_number, account_holder, password, address, phone, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.password = password
        self.address = address
        self.phone = phone
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully: current balance is {self.balance}")
        else:
            print("Invalid deposit amount")
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully: current balance is {self.balance}")
        else:
            print("Insufficient balance")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone}")
        print(f"Balance: {self.balance}")
    
    def verify_password(self, password):
        return self.password == password  # Method to verify password

class BankSystem:
    def __init__(self):
        self.accounts = {}
         
    def create_account(self, account_number, account_holder, address, phone, initial_balance, password):
        if account_number in self.accounts:
            print("Account already exists")
        else:
            new_account = BankAccount(account_number, account_holder, password, address, phone, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account for {account_holder} created successfully")
            
    def login(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.verify_password(password):  # Correct password verification
            print("Login successful")
            return account
        else:
            print("Invalid account or password")
            return None
       
def main():
    bank = BankSystem()
    
    while True:
        print("\nBanking System")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            password = input("Input your password: ")
            address = input("Enter your permanent address: ")
            phone = input("Enter your phone number: ")
            initial_balance = float(input("Enter your initial deposit amount: "))
            bank.create_account(account_number, account_holder, address, phone, initial_balance, password)
                
        elif choice == '2':
            account_number = input("Enter your account number: ")
            password = input("Enter password: ")
            account = bank.login(account_number, password)
            if account:
                while True:
                    print("\nAccount Menu")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Account Info:")
                    print("5. Logout")
                    choice1 = input("Select an option: ")
                    if choice1 == '1':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif choice1 == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif choice1 == '3':
                        account.check_balance()
                    elif choice1 == '4':
                        account.account_info()
                    elif choice1 == '5':
                        print("Logged out successfully")
                        break
            else: 
                print("Invalid option!")
                    
        elif choice == '3':
            print("Thank you for using the banking system")
            break
        else:
            print("Invalid option")
   
if __name__ == "__main__":
    main()
