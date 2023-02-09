##
#  Compute income tax according to the 1913 tax schedule.
#

# Read the income from the user.
income = float(input("Enter the income: "))

# Compute the tax payable.
if income < 50000 :
   tax = income * 0.01
elif income < 75000 :
   tax = 500 + (income - 50000) * 0.02
elif income < 100000 :
   tax = 1000 + (income - 75000) * 0.03
elif income < 250000 :
   tax = 1750 + (income - 100000) * 0.04
elif income < 500000 :
   tax = 7750 + (income - 250000) * 0.05
else :
   tax = 20250 + (income - 500000) * 0.06

# Display the result.
print("The tax payable would be", tax)

