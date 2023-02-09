##
#  Compute the tip based on diners' level of satisfaction.
#

# Read input from the user.
print("Please use the following scale:")
print("  1: Totally satisfied")
print("  2: Satisfied")
print("  3: Dissatisfied")
satisfaction = input("What was your level of satisfaction? ")

amount = float(input("How much was your bill? "))

# Compute the tip.
if satisfaction == "1" :
   tip = amount * 0.20
   sat_str = "totally satisifed"
elif satisfaction == "2" :
   tip = amount * 0.15
   sat_str = "satisfied"
else :
   tip = amount * 0.10
   sat_str = "dissatisfied"

# Display the result.
print("Because you were %s, your tip should be $%.2f." % (sat_str, tip))

