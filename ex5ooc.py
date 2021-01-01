class Account:
    
    def __init__(self,owner,balance):
        self.owner = owner 
        self.balance = balance 
    
    def __str__ (self):
        return "Account Owner: " + self.owner + "\nAccount Balance: " + str (self.balance)

    def deposit (self, amt):
        self.balance = self.balance + amt
        print ( "Deposit accepted")
    
    def withdraw(self, amt):
        if amt > self.balance:
            print ( "too big")
        else:
            self.balance = self.balance - amt
            print ("Withdrawal Accepted")
# 1. Instantiate the class
acct1 = Account('Jose',100)
# 2. Print the object
print(acct1)
# Account owner:   Jose
# Account balance: $100
# 3. Show the account owner attribute
print (acct1.owner)
# 'Jose'
# 4. Show the account balance attribute
print (acct1.balance)
# 100
# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
print (acct1.balance)
# Deposit Accepted
acct1.withdraw(75)
print (acct1.balance)
# Withdrawal Accepted
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
print (acct1.balance)
# Funds Unavailable!
