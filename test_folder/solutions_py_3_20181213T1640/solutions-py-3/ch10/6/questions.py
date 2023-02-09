##
#  This module defines a hierarchy of classes that model exam questions. 
#

## A question with a text and an answer.
#
class Question :
   ## Constructs a question with empty question and answer strings.
   #
   def __init__(self) :
      self._text = ""
      self._answer = ""
      
   ##  Sets the question text.
   #   @param questionText the text of this question
   #
   def setText(self, questionText) :   
      self._text = questionText

   ## Adds text to the end of the question text.
   #  @param text the text to add to the end of the question
   #
   def addText(self, text) :
      self._text = self._text + text

   ## Sets the answer for this question.
   #  @param correctResponse the answer
   #
   def setAnswer(self, correctResponse) :
      self._answer = correctResponse

   ## Checks a given response for correctness.
   #  @param response the response to check
   #  @return True if the response was correct, False otherwise
   #
   def checkAnswer(self, response) :
      return response == self._answer

   ## Displays this question.
   #
   def display(self) :
      print(self._text)   
      
## A question with multiple choices.
#
class ChoiceQuestion(Question) :
   # Constructs a choice question with no choices.
   def __init__(self) :
      super().__init__()
      self._num_choices = 0

   ## Adds an answer choice to this question.
   #  @param choice the choice to add
   #  @param correct True if this is the correct choice, False otherwise
   #
   def addChoice(self, choice, correct) :
      self._num_choices = self._num_choices + 1
      self.addText("\n" + str(self._num_choices) + ": " + choice)
      if correct :
         choiceString = str(self._num_choices)
         self.setAnswer(choiceString)

