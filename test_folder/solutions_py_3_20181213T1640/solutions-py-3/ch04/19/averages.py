##
#  This program computes the average exam grade for multiple students.  It
#  also computes the overall average exam grade.
#

# Obtain the number of exam grades per student.
numExams = int(input("How many exam grades does each student have? "))

# Initialize moreGrades to a non-sentinel value.
moreGrades = "Y"

# Compute average exam grades until the user wants to stop.
overall_total = 0
overall_count = 0
while moreGrades == "Y" :

   # Compute the average grade for one student.
   print("Enter the exam grades.")
   total = 0
   for i in range(1, numExams + 1) :
      score = int(input("Exam %d: " % i))    # Prompt for each exam grade.
      total = total + score

   average = total / numExams
   print("The average is %.2f" % average)

   # Add to the overall total and count for computing the overall average.
   overall_total = overall_total + average
   overall_count = overall_count + 1

   # Prompt as to whether the user wants to enter grades for another student.
   moreGrades = input("Enter exam grades for another student (Y/N)? ")
   moreGrades = moreGrades.upper()

# Display the overall average.
print("The overall average is", overall_total / overall_count)

