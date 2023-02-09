##
#  Read a value from a volt meter and determine the temperature.
#

# Define constants.
V_MIN = 12
V_MAX = 18
K = 0.5
R0 = 100
RS = 75
VS = 20

# Read input from the user.
vm = float(input("Enter the value from the volt meter: "))

# Check that the input is valid.
if vm < V_MIN or vm > V_MAX :
   print("The voltage is outside of the acceptable range.")
else :
   # Compute and display the temperature.
   t = RS / K * vm / (VS - vm) - R0 / K
   print("The temperature is %.2f degrees Celsius." % t)

