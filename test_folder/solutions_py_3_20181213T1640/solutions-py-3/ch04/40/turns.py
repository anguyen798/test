##
#  Determine the turns ratio that maximizes power.
#

# Define constant variables.
R0 = 20
VS = 40
RS = 8
STEP = 0.01

#
#  Compute the power for all values from STEP up to 2, saving the maximum.
#
max_power = 0
n = STEP
while n <= 2 :
   Ps = RS * ((n * VS) / (n * n * R0 + RS)) ** 2
   if Ps > max_power :
      max_power = Ps
      max_turns = n
   n = n + STEP

# Display the result.
print("The maximum power is %.2f with a turns ratio of %.2f." % (max_power, max_turns))

