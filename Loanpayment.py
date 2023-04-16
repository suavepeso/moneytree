# Loan Payment Calculator
print("This is a Loan Payment Plan Calculator, this will help you calculate the best options to pay off your loan.")

loan_amount = float(input("Please enter your loan amount: "))  
interest_rate = 5 / 100  


slowest_rate = interest_rate + 0.01  
slowest_monthly_rate = slowest_rate / 12  
slowest_months = 12 * 5  
slowest_monthly_payment = (loan_amount * slowest_monthly_rate) / (1 - (1 + slowest_monthly_rate) ** (-slowest_months))


fastest_rate = interest_rate - 0.01  
fastest_monthly_rate = fastest_rate / 12 
fastest_months = 12 * 3  
fastest_monthly_payment = (loan_amount * fastest_monthly_rate) / (1 - (1 + fastest_monthly_rate) ** (-fastest_months))


print(f"At the slowest rate, your monthly payment will be ${round(slowest_monthly_payment, 2)} for a 5-year term.")
print(f"At the fastest rate, your monthly payment will be ${round(fastest_monthly_payment, 2)} for a 3-year term.")
