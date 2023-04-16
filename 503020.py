#50/30/20 Calculator
print("This is a Savings Calculator using the 50, 30, 20 Method!")

def savings_calculator():
    paycheck = float(input("Enter your paycheck amount: "))
    needs = paycheck * 0.5
    wants = paycheck * 0.3
    savings = paycheck * 0.2
    
    print(f"Your paycheck is: ${paycheck:.2f}")
    print(f"The 50% of your paycheck that should be used for needs is: ${needs:.2f}")
    print(f"The 30% of your paycheck that should be used for wants is: ${wants:.2f}")
    print(f"The 20% of your paycheck that should be used for savings is: ${savings:.2f}")

savings_calculator()

