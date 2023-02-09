##
#  Generate junk mail from a database and a template.
#

# Read the template.
template_file = open("template", "r")
template = template_file.read()

# Close the template file.
template_file.close()

# Generate a new file for each line in the database.
database_file = open("database", "r")
for line in database_file :
   parts = line.split("|")

   # Save the result of inserting the current line from the database into
   # the template.
   outf = open(parts[1] + parts[2] + ".txt", "w")

   complete_letter = template
   for i in range(0, 7) :
      complete_letter = complete_letter.replace("|%d|" % (i + 1), parts[i])
   outf.write(complete_letter)

   # Close the output file.
   outf.close()

# Close the database file.
database_file.close()

