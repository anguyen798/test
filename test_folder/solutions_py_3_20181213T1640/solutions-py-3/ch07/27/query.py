##
#  Query three files containing personal information.
#

# Read the phone number from the user.
phone = input("Enter the phone number (7 digits, with a dash): ")

# Try to connect the phone number to a name.
name = ""
inf = open("data1.txt", "r")
for line in inf :
   parts = line.rstrip().split(",")
   if parts[1].strip() == phone :
      name = parts[0].strip()
inf.close()

# Display the result of the phone number search.
if name == "" :
   print("Couldn't find a name associated with that number.")
else :
   print(phone, "is associated with", name)

   # Try to connect the name with a SSN.
   ssn = ""
   inf = open("data2.txt", "r")
   for line in inf :
      parts = line.rstrip().split(",")
      if parts[0] == name :
         ssn = parts[1].strip()
   inf.close()

   # Display the result of the name search.
   if ssn == "" :
      print("Couldn't find a SSN for", name)
   else :
      print("%s's SSN is %s" % (name, ssn))

      # Try to connect the SSN to a salary.
      salary = ""
      inf = open("data3.txt", "r")
      for line in inf :
         parts = line.rstrip().split(",")
         if parts[0] == ssn :
            salary = parts[1].strip()
      inf.close()
   
      # Display the result of the SSN search.
      if salary == "" :
         print("Couldn't find a salary for", name)
      else :
         print("%s's SSN is %s" % (name, salary))
   

