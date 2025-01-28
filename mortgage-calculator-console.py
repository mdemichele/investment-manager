# Description: This is just a simple function that lets you calculate your monthly mortgage payments

def mortgageCalc(principal, loan_length, annual_interest):
    """Returns the monthly mortgage payment given home price, down_payment, length of loan, and interest_rate"""
    
    # Basic Formula: M = P[r(1 + r) ^ n / (1 + r) ^ n - 1]
    
    # First, calculate the monthly interest rate from the annual interest rate
    # To do so: take annual_interest and divide by 12 
    monthly_interest = (annual_interest / 100) / 12
    
    # Second, calculate the total number of payments over the loan's lifetime
    # To do so: Take loan_length and multiply by 12
    total_payments = loan_length * 12
    
    # Third use the calculated values to get the dividend (top) and divisor (bottom) of the Formula
    dividend = monthly_interest * (1 + monthly_interest) ** total_payments
    divisor  = (1 + monthly_interest) ** total_payments - 1
    
    # Get the quotient by dividing the dividend by the divisor
    quotient = dividend / divisor
    
    # Finally, multiply quotient by the principal loan amount to get the monthly mortgage payment
    monthly_payment = principal * quotient
    
    return int(monthly_payment)
    

def main():
    # Say, purchase price is $600,000. You put down 10% plus closing costs. So, you borrow $540,000
    principal = input("Please enter the Principal: ")
    loan_length = input("Please enter the Loan Length: ")
    annual_interest = input("Please enter the Annual Interest: ")

    monthly_payment = mortgageCalc(int(principal), int(loan_length), float(annual_interest))

    print("Your monthly payment on Principal and Interest will be approximately: $" + str(monthly_payment))

if __name__ == "__main__":
    main()