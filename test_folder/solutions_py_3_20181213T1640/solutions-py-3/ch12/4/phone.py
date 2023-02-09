from binarysearch import binarySearch

# Read the database into parallel lists for the names and the numbers.
names = []
nums = []
inf = open("data.txt", "r")
for line in inf :
   parts = line.split("|")
   names.append(parts[0])
   nums.append(parts[1])
inf.close()

# Let the user look up names and numbers until they choose to quit.
choice = input("L)ookup Name, Lookup N)umber or Q)uit? ").upper()
while choice != "Q" :
   # Look up the number associated with a name.
   if choice == "L" :
      name = input("Enter the name: ")
      pos = binarySearch(names, 0, len(names) - 1, name)
      if pos == -1 :
         print("Sorry, no match was found.")
      else :
         print("The number is:", nums[pos])
      
   # Look up the name associated with a number.
   elif choice == "N" :
      num = input("Enter the number: ")
      pos = binarySearch(nums, 0, len(nums) - 1, num)
      if pos == -1 :
         print("Sorry, no match was found.")
      else :
         print("The name is:", names[pos])

   # Handle an invalid choice.
   elif choice != "Q" :
      print("That wasn't a valid choice.")

   # Get the next choice from the user.
   choice = input("L)ookup Name, Lookup N)umber or Q)uit? ").upper()

