##
#  Define the grade class.
#

##
#  A letter grade that can be converted to a number of grade points.
class Grade :
   ## Construct a new letter grade.
   #  @param letter the letter grade to store
   def __init__(self, letter) :
      self._letter = letter

   ## Get the number of grade points assoicated with the grade.
   #  @return the number of grade points
   def getGradePoints(self) :
      GRADE_POINTS = {"A+": 4.3, "A": 4, "A-": 3.7, "B+": 3.3, "B": 3, "B-":
         2.7, "C+": 2.3, "C": 2, "C-": 1.7, "D+": 1.3, "D": 1, "D-": 0.7, 
         "F": 0}

      return GRADE_POINTS[self._letter]

