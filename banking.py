"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""

accounts = {}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    if account_number not in accounts:
        accounts[account_number] = {
            "name": name,
            "balance": 0.0
        }
        #Add optional features (e.g., overdraft_limit, account_type, etc.)
        for key, value in kwargs.items():
            accounts[account_number][key] = value
    else:
        print(f"Account {account_number} already exists.")

create_account(8033806964, "Alice", overdraft_limit = 500)
create_account(9029159123, "Bob")  
#print(accounts)  
#pass

def deposit(account_number, amount):
    """Deposit money into account.
        return "Account not found!" (if account does not exists)
        return Deposited {amount} into {accounts name}'s account. if account exists
    """
    if account_number in accounts:
        accounts[account_number]["balance"] += amount
    else:
        print("account not found")    

deposit(8033806964, 1000)
deposit(9029159123, 1000)
print(accounts)     

#pass

def withdraw(account_number, amount):
    """Withdraw money if balance is sufficient. else: insufficient funds"""
    if account_number in accounts:
        if accounts[account_number]["balance"] >= amount:
            accounts[account_number]["balance"] -= amount
            print(f"{amount} withdrawn from {account_number}")
        else:
            print("insufficient fund") 
    else:
        print("account does not exist") 
withdraw(8033806964, 100)      
print(accounts)
    #pass

def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts. if funds is sufficient"""
    if from_acc in accounts:
        if to_acc in accounts:
            if accounts[to_acc]["balance"] >= amount:
                accounts[from_acc]["balance"] -= amount
                accounts[to_acc]["balance"] += amount
                print(f"{amount} deposited from {from_acc} to {to_acc}")
            else:
                print("insufficient balance")    
        else:
            print("destination account does not exist")
    else:
        print("source account does not exist") 
transfer(8033806964, 9029159123, 200)
print(accounts)                   
pass
