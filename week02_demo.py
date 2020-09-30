# Initial balance of the bank account
'''
initial_balance = 200
'''

# Bank statement with all transactions for the past 6 months
'''
statement = [[-119.02, -56.54, 1200, -80, -12.99, -550, -167.90, -5.58, -3.54, -9.99],
             [-138.32, -67.12, 1200, -80, -12.99, -268.10, -550, -92.90, -125.65],
             [-101.44, -48.83, -19.99, -92.12, 1200, -80, -67.33, -12.99, -550, -30.33],
             [-91.98, -45.65, -50, -9.99, 1200, -80, -414.22, -12.99, -550, -9.29, -67.12],
             [-159.53, -27.61, -168.45, 1200, -80, -12.99, -76.94, -550, -28.08, -27.89],
             [-141.97, 1200, -87.78, -80, -12.99, -67.92, -188.09, -550, -4.20, -13.68]]
'''

# Your job: pay monthly 0.5% interest to this account.

# Update the account balance each month: OK!
# Calculate interest each month: OK!
# Pay the total interest (6 months) to the account:
# - pay the total (update the balance for the last month)
# - log that transaction into statement for 6th month.

def update_balance(month, starting_balance):
    balance = starting_balance + sum(month)
    return round(balance,2)

example_month = [100,-20,-30,100,90]
example_starting_balance = 20
update_balance(example_month, example_starting_balance)

def calculate_interest(balance, interest_rate):
    '''
    Returns total interest paid for a given balance,
    at rate interest_rate (given in %).
    '''
    interest = 0.01 * interest_rate * balance
    return round(interest,2)

example_balance = update_balance(example_month, example_starting_balance)
example_interest_rate = 0.5
calculate_interest(example_balance, example_interest_rate)

def update_statement(statement, initial_balance, interest_rate):
    '''
    Update the client's bank statement with interest payment.
    '''
    balance = initial_balance
    total_interest = 0
    
    for month in statement:
        balance = update_balance(month, balance)
        total_interest = total_interest + calculate_interest(balance, interest_rate)
    
    '''
    Get out of the loop and update the interest of the last month.
    '''
    statement[-1].append(total_interest)
    '''
    See the final balance after counting in the interest and return the balance.
    This is not necessary.
    Updating the statement's interest is enough.
    '''
    balance = balance + total_interest

    return statement, balance

example_statement = [[10,-20,30,20],
                     [2,0.9,-90],
                     [9,8,-20,40]]
exapmel_initial_balance = 200
example_interest_rate = 0.5
update_statement(example_statement,exapmel_initial_balance,example_interest_rate)

statement = [[-119.02, -56.54, 1200, -80, -12.99, -550, -167.90, -5.58, -3.54, -9.99],
             [-138.32, -67.12, 1200, -80, -12.99, -268.10, -550, -92.90, -125.65],
             [-101.44, -48.83, -19.99, -92.12, 1200, -80, -67.33, -12.99, -550, -30.33],
             [-91.98, -45.65, -50, -9.99, 1200, -80, -414.22, -12.99, -550, -9.29, -67.12],
             [-159.53, -27.61, -168.45, 1200, -80, -12.99, -76.94, -550, -28.08, -27.89],
             [-141.97, 1200, -87.78, -80, -12.99, -67.92, -188.09, -550, -4.20, -13.68]]
initial_balance = 200
interest_rate = 0.5
update_statement(statement,initial_balance,interest_rate)