##
#  Define a class to represent a combination lock.
#

##
#  A class that simulates locking and unlocking a combination lock.
class ComboLock :
   ## Construct a new combination lock with the provided secret code.
   #  @param secret1 the first digit in the combination
   #  @param secret2 the second digit in the combination
   #  @param secret3 the third digit in the combination
   #
   def __init__(self, secret1, secret2, secret3) :
      self._secret1 = secret1
      self._secret2 = secret2
      self._secret3 = secret3
      self._turns = []

   ## Reset the combination lock.
   #
   def reset(self) :
      self._turns = []

   ## Turn the lock to the left.
   #  @param ticks the number of ticks to turn
   #
   def turnLeft(self, ticks) :
      self._turns.append(ticks)

   ## Turn the lock to the right.
   #  @param ticks the number of ticks to turn
   #
   def turnRight(self, ticks) :
      self._turns.append(-ticks)

   ## Attempt to open the lock.
   #  @return True if the lock opens, False otherwise
   #
   def open(self) :
      # The user did not make the correct number of turns.
      if len(self._turns) != 3 :
         return False
      # The user did not turn in the correct directions.
      if self._turns[0] >= 0 or self._turns[2] >= 0 or self._turns[1] <= 0 :
         return False

      num1 = self._turns[0] % 40
      num2 = (num1 + self._turns[1]) % 40
      num3 = (num2 + self._turns[2]) % 40
      print(num1, num2, num3)

      return num1 == self._secret1 and \
             num2 == self._secret2 and \
             num3 == self._secret3

