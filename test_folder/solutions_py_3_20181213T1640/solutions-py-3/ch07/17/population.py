##
#  Compute the total population.
#

# Open the populuation file.
inf = open("worldpop.txt")

# Compute the total population.
total = 0
for line in inf :
   name = ""
   pop_str = ""
   i = 0
   while i < len(line) :
      # Handle characters that are part of a country name.
      if line[i] >= "a" and line[i] <= "z" or \
         line[i] >= "A" and line[i] <= "Z" or line[i] in "()-,":
         name = name + line[i]
      # Handle whitespace.
      elif line[i] == " " or line[i] == "\t" :
         while line[i] == " " or line[i] == "\t" :
            i = i + 1
         if line[i] < "0" or line[i] > "9" :
            name = name + " "
            name = name + line[i]
         else :
            pop_str = pop_str + line[i]
      # Handle characters that are part of the population number.
      elif line[i] >= "0" and line[i] <= "9" :
         pop_str = pop_str + line[i]

      i = i + 1

   pop = int(pop_str)
   if name != "European Union" :
      total = total + pop

# Close the input file.
inf.close()

# Display the total population.
print("The total population is", pop)
     

