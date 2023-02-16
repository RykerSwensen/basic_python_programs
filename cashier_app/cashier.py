# This is a basic program developed to emulate a cashier program in Python.

# Get user information on prices, people, and sales tax
price_of_childs_meal = float(input('What is the price of the childs meal? '))
price_of_adults_meal = float(input('What is the price of the adults meal? '))
sales_tax_rate = float(input('What is the sales tax rate?' ))
children = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))

# Get the sub total.
sub_total = (price_of_childs_meal * children) + (price_of_adults_meal * adults)

# Compute total sales tax
sales_tax = (sub_total * sales_tax_rate) / 100

# Compute total cost.
total = sub_total + sales_tax

print(f'The sub total is ${sub_total:.2f}.')
print(f'The sales tax is ${sales_tax:.2f}.')
print(f'The total cost after sales tax is ${total:.2f}.')
print()

# Ask if the user would like to add a tip.
tip = input('Would you like to leave a tip? ')

if tip == 'yes':
    print(f'Thank you, the suggested tip amounts are; 10%, 15%, & 20%')
    print()

    # If the user chooses to leave a tip, ask for the perccentage.
    total_plus_tip = float(input('Please enter the percentage tip you would like to leave in decimal form.'))
    print()
    grand_total = total + (total * total_plus_tip)
    print(f'Thank you for your tip of {total_plus_tip:.2f} percent, your grand total today is ${grand_total:.2f}.')
    print()
elif tip == 'no':
    print('You are a cheapskate, please do not return to our establishment.')
    grand_total = total + 0
    print()

# Get the amount the user is paying with.
payment_amount = float(input('What is the payment amount? '))

# Compute change.
change = payment_amount - grand_total
if payment_amount >= total:
    print(f'Thank you for providing adequate funds, your change today is ${change:.2f}.')
else:
    print(f'You are going to have to do better than that. You still owe ${change:.2f}.')
