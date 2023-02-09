##
#  Simulate how stalls fill in a restroom.
#

# Define constants.
NUM_STALLS = 11

# Start with all of the stalls unoccupied.
occupied = []
for i in range(0, NUM_STALLS) :
   occupied.append(False)

# Loop as long as there is an unoccupied stall.
while False in occupied :
   # Find the position and length of the longest run.
   longest_length = 0
   longest_pos = 0
   for i in range(0, len(occupied)) :
      if occupied[i] == False :
         current_length = 1
         pos = i + 1
         while pos < len(occupied) and occupied[pos] == False :
            current_length = current_length + 1
            pos = pos + 1
         if current_length > longest_length :
            longest_length = current_length
            longest_pos = i

   # Fill in the middle position in the longest unoccupied run.
   occupied[longest_pos + longest_length // 2] = True
   
   # Display the currently used / unused stalls.
   for i in range(0, len(occupied)) :
      if occupied[i] :
         print("X ", end="")
      else :
         print("- ", end="")
   print()

