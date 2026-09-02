"""
Abstractions.
Bank class -->
deposits, withdrawal,
show account
getter and setter. -->
--> easy to scale function <understanding>
-------------------------------------------------
--> Login to account
--> Create account
--> Deposit
--> Withdrawal
--> Check balance
"""

class BankAccount:

    def __init__(self,name, balance,account_no):
        self.name=name
        self.balance=balance
        self.account_no=account_no

    #later change it to a getter
    def get_balance(self):
        pass

    #setter
    def deposit(self):
        pass

    def withdrawal(self):
        pass

    def show_account_details(self):
        print(f"Owner {self.name}")
        print(f"Balance {self.balance}")
        print(f"Account No {self.account_no}")

john=BankAccount(name="John Mwangi", balance=0,account_no="123456")

john.show_account_details()