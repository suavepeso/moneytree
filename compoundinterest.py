def compound_interest(principal, rate, time):
    return principal * (1 + rate)**time

initial_savings = float(input("How much have you already saved? "))
monthly_savings = float(input("How much do you plan to 2save each month? "))
interest_rate = 0.05

for year in range(1, 101):
    total_savings = initial_savings
    for month in range(1, 13):
        savings_this_month = compound_interest(monthly_savings, interest_rate/12, (year-1)*12 + month)
        total_savings += savings_this_month
    print("After {} years, your savings would be {:.2f}".format(year, total_savings))
