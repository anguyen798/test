##
#  This module defines the student class.
#

##
#  A student with a name and a total quiz score.
class Student :
   ## Constructs a new student with the provided name.
   #  @param name the name of the student
   def __init__(self, name) :
      self._name = name
      self._score = 0
      self._num_quizes = 0

   ## Gets the name of the student.
   #  @return the name of the student
   def getName(self) :
      return self._name

   ## Adds a quiz score to the student's total.
   #  @param score the score for the quiz
   def addQuiz(self, score) :
      self._score = self._score + score
      self._num_quizes = self._num_quizes + 1

   ## Gets the total score on the quizes.
   #  @return the student's total score on the quizes
   def getTotalScore(self) :
      return self._score

   ## Get the average score for the student.
   #  @return the average score for the student's quizes
   def getAverageScore(self) :
      return self._score / self._num_quizes

