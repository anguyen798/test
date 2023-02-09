##
#  Determine if the door to a minivan can be opened given the status of
#  various switches.
#

# Read the switch positions from the user.
db_left = bool(int(input("Left dashboard switch (0 or 1): ")))
db_right = bool(int(input("Right dashboard switch (0 or 1): ")))
child_lock = bool(int(input("Child lock switch (0 or 1): ")))
master_unlock = bool(int(input("Master unlock switch (0 or 1): ")))
inside_left = bool(int(input("Left inside handle (0 or 1): ")))
outside_left = bool(int(input("Left outside handle (0 or 1): ")))
inside_right = bool(int(input("Right inside handle (0 or 1): ")))
outside_right = bool(int(input("Right outside handle (0 or 1): ")))
gear_shift = input("Gear shift position (P, N, D, 1, 2, 3 or R): ")

# Determine which doors open.
leftOpens = False
rightOpens = False

if master_unlock and gear_shift == "P" :
   if db_left or not child_lock and inside_left or outside_left :
      leftOpens = True
   if db_right or not child_lock and inside_right or outside_right :
      rightOpens = True

# Display the result.
if leftOpens and rightOpens :
   print("Both doors open.")
elif leftOpens :
   print("Left door opens.")
elif rightOpens :
   print("Right door opens.")
else :
   print("Both doors stay closed.")

