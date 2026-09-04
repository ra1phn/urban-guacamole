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
    clients=0 # static
    bank_name="Post Bank" # static property

    def __init__(self,name, balance,account_no):
        self.name=name
        self._balance=balance
        self.account_no=account_no

    #data I read
    @property
    def balance(self):
        print("Someone tried to read John's balance")
        return self._balance

    #to control updated
    @balance.setter
    def deposit(self, value):
        if not isinstance(value,(int,float)):
            print("Ensure you pass a number for new balance")
            return
        if value <0:
            print("Ensure new balance must not be less than 0")
            return
        self.balance=value

    def deposit(self):
        pass

    def withdrawal(self):
        pass

    def show_account_details(self):
        print(f"Owner {self.name}")
        print(f"Balance {self.balance}")
        print(f"Account No {self.account_no}")

john=BankAccount(name="John Mwangi", balance=0,account_no="123456")

# john.show_account_details()
print("Bank Name:", BankAccount.bank_name)
print(john.account_no) # John
print("Clients:", BankAccount.clients) #class property
