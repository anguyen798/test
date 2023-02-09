##
#  Count how many times each word occurs in a file.  Cache the results to avoid
#  performing the same count multiple times.
#

# Create the cache.
cache = {}

# Read the file name from the user and open the file.
filename = input("Enter the name of a file (or quit to quit): ")

# Loop until the user chooses to quit.
while filename != "quit" :
   # Handle the case where we have read the file previously.
   if filename in cache :
      counts = cache[filename]
   # Handle the case where we have not read the file previously.
   else :
      inf = open(filename, "r")
   
      # Create a new empty dictionary.
      counts = {}
   
      # Count the words in the file.
      for line in inf :
         words = line.split()
         for word in words :
            if word in counts :
               counts[word] = counts[word] + 1
            else :
               counts[word] = 1
   
      # Close the file.
      inf.close()
      
      # Store the counts into the cache.
      cache[filename] = counts
   
   # Display the counts.
   for word in sorted(counts):
      print("%s: %d" % (word, counts[word]))

   # Read the next file name from the user.
   filename = input("Enter the name of a file (or quit to quit): ")

