##
#  Sort a bunch of strings by their lengths.
#

# Read some data from the user.
data = []
s = input("Enter a string (empty to quit): ")
while s != "" :
   data.append(s)
   s = input("Enter a string (empty to quit): ")

# Sort the string by comparing their lengths.
data = sorted(data, key=len)

# Display the result.
print("Sorting the strings by length gives:")
print(data)

