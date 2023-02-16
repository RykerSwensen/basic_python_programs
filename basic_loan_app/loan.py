# This is a simple loan approval/denial program.
# You judge the users input to see if they can be 
# approved for a loan!

loan_amount = int(input('On a scale from 1-10, how big is the loan amount you are requesting? '))

credit_score = int(input('On a scale from 1-10, how good is your credit score? '))

income = int(input('On a scake fron 1-10, how high is your annual income? '))

down_payment = int(input('On a scale from 1-10, how big is your downpayment in comparison to your requested loan? '))

if loan_amount >= 5:
    if income >= 7 and down_payment >=7:
        print('Congratulations! You are pre approved for your requested loan!')
    else:
        print('Sorry, your loan was not approved. Better luck next time.')
elif loan_amount < 5:
    if credit_score < 4:
        print('Sorry, your loan was not approved. Better luck next time.')
    elif income >= 7 or down_payment >= 7:
        print('Congratulations! You are pre approved for your requested loan!')
    elif income >= 4 and down_payment >= 4:
        print('Congratulations! You are pre approved for your requested loan!')
    else:
       print('Sorry, your loan was not approved. Better luck next time.')
else:
    print('Sorry!')