##
#  Define a class to represent a voting machine.
#

# A voting machine that keeps track of votes for each of two parties.
class VotingMachine :

   ## Construct a new voting machine.
   #
   def __init__(self) :
      self._dem_count = 0
      self._rep_count = 0

   ## Record a vote for a democrat.
   #
   def voteDemocrat(self) :
      self._dem_count = self._dem_count + 1

   ## Record a vote for a republican.
   #
   def voteRepublican(self) :
      self._rep_count = self._rep_count + 1

   ## Get the tallies for both parties.
   #  @return a tuple with the democrat count first and the republican count second
   #
   def getTallies(self) :
      return (self._dem_count, self._rep_count)

   ## Reset the voting machine.
   #
   def reset(self) :
      self._dem_count = 0
      self._rep_count = 0

