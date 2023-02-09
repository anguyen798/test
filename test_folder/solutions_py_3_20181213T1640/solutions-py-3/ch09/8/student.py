##
#  This module defines the student class.
#
from grade import Grade

##
#  A student with a name and a quiz GPA.
class Student :
   ## Constructs a new student with the provided name.
   #  @param name the name of the student
   def __init__(self, name) :
      self._name = name
      self._grade_points = 0
      self._num_quizes = 0

   ## Gets the name of the student.
   #  @return the name of the student
   def getName(self) :
      return self._name

   ## Adds a quiz grade to the student's total.
   #  @param grade the grade for the quiz
   def addQuiz(self, grade) :
      self._grade_points = self._grade_points + grade.getGradePoints()
      self._num_quizes = self._num_quizes + 1

   ## Gets the total grade points on the quizes.
   #  @return the student's total grade points for all of the quizes
   def getTotalScore(self) :
      return self._grade_points

   ## Get the average grade points for the student.
   #  @return the average grade points for the student's quizes
   def getAverageScore(self) :
      return self._grade_points / self._num_quizes

