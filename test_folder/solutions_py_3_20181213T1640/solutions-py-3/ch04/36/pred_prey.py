##
#  Model the relationships between predators and prey.
#

# Read the simulation parameters from the user.
a = float(input("Enter the value for A (0.1 is a good choice): "))
b = float(input("Enter the value for B (0.01 is a good choice): "))
c = float(input("Enter the value for C (0.01 is a good choice): "))
d = float(input("Enter the value for D (0.00002 is a good choice): "))

prey = int(input("Enter the initial prey (1000 is a good choice): "))
preds = int(input("Enter the initial predators (20 is a good choice): "))

periods = int(input("Enter the number of periods: "))

# Run the simulation for the requested the of periods.
for period in range(1, periods + 1) :
   new_prey = prey * (1 + a - b * preds)
   new_preds = preds * (1 - c + d * prey)

   print("After period", period, "there are", round(new_preds), "predators")
   print("After period", period, "there are", round(new_prey), "prey")
   print()

   # Update prey and predators with the newly computed values.
   prey = new_prey
   preds = new_preds

