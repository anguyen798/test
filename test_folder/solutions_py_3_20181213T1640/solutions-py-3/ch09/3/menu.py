##
#  This module defines the Menu class.
#

## A menu that is displayed in the terminal window.
#
class Menu :
   ## Constructs a menu with no options.
   #
   def __init__(self) :
      self._options = ""
      self._num_options = 0
   
   ## Adds an option to the end of this menu.
   #  @param option the option to add
   #
   def addOption(self, option) :
      self._num_options = self._num_options + 1
      self._options = self._options + str(self._num_options) + " " + option + "\n"
   
   ## Displays the menu, with options numbered starting with 1, and prompts
   #  the user for input. Repeats until a valid input is supplied.
   #  @return the number that the user supplied
   #
   def getInput(self) :
      done = False
      while not done :
         print(self._options)
    
         userChoice = int(input())
         if userChoice >= 1 and userChoice <= self._num_options :
            done = True
           
      return userChoice

