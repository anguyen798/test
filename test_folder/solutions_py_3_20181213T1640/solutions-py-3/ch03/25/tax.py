##
#  Compute the tax payable based on income and marital status.
#

# Gather input from the user.
status = input("Are you married or single (M or S)? ")
status = status.upper()

income = float(input("What is your income? "))

# Compute the tax payable.
if status == "S" :
   if income >= 0 and income <= 8000 :
      tax = income * 0.10
   elif income > 8000 and income <= 32000 :
      tax = 800 + (income - 8000) * 0.15
   elif income >= 32000 :
      tax = 4400 + (income - 32000) * 0.25
elif status == "M" :
   if income >= 0 and income <= 16000 :
      tax = income * 0.10
   elif income > 16000 and income <= 64000 :
      tax = 1600 + (income - 16000) * 0.15
   elif income >= 64000 :
      tax = 8800 + (income - 64000) * 0.25

# Display the result.
print("Your tax payable is", tax)

