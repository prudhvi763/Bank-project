import sqlite3
import random as r

class Bank:
    print("WELCOME TO SBI BANK")
    print("-------------------")
    
    def __init__(self):
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()
        print("SQLite is connected")
    
    def create_account(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS Bank (
                            account_name TEXT,
                            acc_no INTEGER,
                            balance INTEGER
                         )""")
        n1 = input("Enter Your First Name: ").upper()
        n2 = input("Enter Your Last Name: ").upper()
        print("---------------------------------------")
        if n1.isalpha() and n2.isalpha() and len(n1) > 2 and len(n2) > 2:
            name = f"{n1} {n2}"
            num = r.randint(10000000, 99999999)
            balance = 0
            self.c.execute("INSERT INTO Bank VALUES (?, ?, ?)", (name, num, balance))
            print(f"Hello {name}, your account has been created. Note your account number.")
            print(f"Your Account Number is: {num}")
            print("---------------------------------------")
            self.con.commit()
        else:
            print("Invalid name. Please try again.")
    
    def open_account(self):
        print("------------------------------")
        a_num = int(input("Enter the Account Number: "))
        check = True
        flag = False
        for a, b, c in self.c.execute("SELECT * FROM Bank"):
            if b == a_num:
                flag = True
                check = False
                val = c
                na = a
                print("(c) - Check Balance")
                print("(d) - Deposit")
                print("(w) - Withdraw")
                ope = input("Enter any of the operations (c)/(d)/(w): ").lower()
                
                if ope == 'd':
                    dep = int(input("Enter the Amount to Deposit: "))
                    deposit = dep + val
                    self.c.execute("UPDATE Bank SET balance = ? WHERE acc_no = ?", (deposit, a_num))
                    self.con.commit()
                    print(f"Amount Deposited: {dep} ₹. Available Balance: {deposit} ₹")
                
                elif ope == 'w':
                    wit = int(input("Enter the Amount to Withdraw: "))
                    if val > 0 and val >= wit:
                        withdraw_bal = val - wit
                        self.c.execute("UPDATE Bank SET balance = ? WHERE acc_no = ?", (withdraw_bal, a_num))
                        self.con.commit()
                        print(f"Withdrawn {wit} ₹ successfully. Available balance: {withdraw_bal} ₹")
                    else:
                        print("Insufficient balance.")
                
                elif ope == 'c':
                    print(f"Hello {na}, Your Account Balance is {val} ₹")
                else:
                    print("Invalid operation.")
        
        if check:
            print("Invalid Account Number.")
        print("----------------------------------------------------------")

# Main code
bk = Bank()
print("(c) - Create Account")
print("(o) - Open Account")
op = input("Enter your choice (c)/(o): ").lower()
if op == 'c':
    bk.create_account()
elif op == 'o':
    bk.open_account()
else:
    print("Invalid choice.")
