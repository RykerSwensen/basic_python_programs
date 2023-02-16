# This is a basic Python application used to add users accounts and balances into lists.

# Prompt the user to let them know they are in the bank application.
print("Enter the names and balances of bank accounts (type: quit to quit the application)")

# Make a list for accounts. 
account_list = []

# Make a variable for account.
account = None

# Make a list for balances. 
balance_list = []

# Make a variable for balance.
balance = None


# While loop to keep adding accounts until the user wants to stop. 
while account != "quit":
    account = input("Account: ")

    # Until the user says to quit, 
    # keep adding their input to the list.
    if account != "quit":
        account_list.append(account)
        print(account_list)

# While loop to keep adding balances until the user wants to stop.
while balance != "quit":
    balance = (input("balance: "))

    # Until the user says to quit, 
    # keep adding the input to the balances list.
    if balance != "quit":
        balance_list.append(balance)
        print(balance_list)


