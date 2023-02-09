##
#  Compute income tax payable using the 2012 tax brackets.
#

# Initialize constant variables for the tax rates and rate limits.
RATE1 = 0.10
RATE2 = 0.15
RATE3 = 0.25
RATE4 = 0.28
RATE5 = 0.33
RATE6 = 0.35

R1_S_LIMIT = 8700
R2_S_LIMIT = 35350
R3_S_LIMIT = 85650
R4_S_LIMIT = 178650
R5_S_LIMIT = 388350

R1_M_LIMIT = 17400
R2_M_LIMIT = 70700
R3_M_LIMIT = 142700
R4_M_LIMIT = 217450
R5_M_LIMIT = 388350

# Read income and marital status.
income = float(input("Please enter your income: "))
maritalStatus= input("Please enter s for single, m for married: ")

# Compute taxes due.
tax1 = 0.0
tax2 = 0.0
tax3 = 0.0
tax4 = 0.0
tax5 = 0.0
tax6 = 0.0

if maritalStatus == "s" :
   # Compute taxes for a single person.
   if income < R1_S_LIMIT :
      tax1 = RATE1 * income
   elif income < R2_S_LIMIT :
      tax1 = RATE1 * R1_S_LIMIT
      tax2 = RATE2 * (income - R1_S_LIMIT)
   elif income < R3_S_LIMIT :
      tax1 = RATE1 * R1_S_LIMIT
      tax2 = RATE2 * (R2_S_LIMIT - R1_S_LIMIT)
      tax3 = RATE3 * (income - R2_S_LIMIT)
   elif income < R4_S_LIMIT : 
      tax1 = RATE1 * R1_S_LIMIT
      tax2 = RATE2 * (R2_S_LIMIT - R1_S_LIMIT)
      tax3 = RATE3 * (R3_S_LIMIT - R2_S_LIMIT)
      tax4 = RATE4 * (income - R3_S_LIMIT)
   elif income < R5_S_LIMIT :
      tax1 = RATE1 * R1_S_LIMIT
      tax2 = RATE2 * (R2_S_LIMIT - R1_S_LIMIT)
      tax3 = RATE3 * (R3_S_LIMIT - R2_S_LIMIT)
      tax4 = RATE4 * (R4_S_LIMIT - R3_S_LIMIT)
      tax5 = RATE5 * (income - R4_S_LIMIT)
   else :
      tax1 = RATE1 * R1_S_LIMIT
      tax2 = RATE2 * (R2_S_LIMIT - R1_S_LIMIT)
      tax3 = RATE3 * (R3_S_LIMIT - R2_S_LIMIT)
      tax4 = RATE4 * (R4_S_LIMIT - R3_S_LIMIT)
      tax5 = RATE5 * (R5_S_LIMIT - R4_S_LIMIT)
      tax6 = RATE6 * (income - R5_S_LIMIT)
else :
   # Compute taxes for a married couple.
   if income < R1_M_LIMIT :
      tax1 = RATE1 * income
   elif income < R2_M_LIMIT :
      tax1 = RATE1 * R1_M_LIMIT
      tax2 = RATE2 * (income - R1_M_LIMIT)
   elif income < R3_M_LIMIT :
      tax1 = RATE1 * R1_M_LIMIT
      tax2 = RATE2 * (R2_M_LIMIT - R1_M_LIMIT)
      tax3 = RATE3 * (income - R2_M_LIMIT)
   elif income < R4_M_LIMIT : 
      tax1 = RATE1 * R1_M_LIMIT
      tax2 = RATE2 * (R2_M_LIMIT - R1_M_LIMIT)
      tax3 = RATE3 * (R3_M_LIMIT - R2_M_LIMIT)
      tax4 = RATE4 * (income - R3_M_LIMIT)
   elif income < R5_M_LIMIT :
      tax1 = RATE1 * R1_M_LIMIT
      tax2 = RATE2 * (R2_M_LIMIT - R1_M_LIMIT)
      tax3 = RATE3 * (R3_M_LIMIT - R2_M_LIMIT)
      tax4 = RATE4 * (R4_M_LIMIT - R3_M_LIMIT)
      tax5 = RATE5 * (income - R4_M_LIMIT)
   else :
      tax1 = RATE1 * R1_M_LIMIT
      tax2 = RATE2 * (R2_M_LIMIT - R1_M_LIMIT)
      tax3 = RATE3 * (R3_M_LIMIT - R2_M_LIMIT)
      tax4 = RATE4 * (R4_M_LIMIT - R3_M_LIMIT)
      tax5 = RATE5 * (R5_M_LIMIT - R4_M_LIMIT)
      tax6 = RATE6 * (income - R5_M_LIMIT)

totalTax = tax1 + tax2 + tax3 + tax4 + tax5 + tax6

# Print the results.
print("The tax is $%.2f" % totalTax)

