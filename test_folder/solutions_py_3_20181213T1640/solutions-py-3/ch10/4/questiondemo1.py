##
#  This program shows a simple quiz with one question.
#

from questions import AnyCorrectChoiceQuestion

# Create the question and expected answer.
q = AnyCorrectChoiceQuestion()
q.setText("Of Apple, Tomato, Carrot, Cucumber and Celery, which is a fruit?")
q.setAnswer("Apple Tomato")      

# Display the question and obtain user's response.
q.display()
response = input("Your answer: ")
print(q.checkAnswer(response))

