##
#  Solve the 8-Queens problem using backtracking.
#

def main() :
   # Find all of the solutions to the 8 queens problem.
   eq = EightQueensPartialSolution()
   sols = solve(eq)
   for s in sols:
      print(s)

## Model a general partial solution to a problem.  This is an abstract class.
#
class PartialSolution() :
   ACCEPT = 0
   ABANDON = 1
   CONTINUE = 2

   ## Examine a partial solution to see if it is acceptable, is not done, but
   #  should be continued, or should be abandoned.
   #  @return ABANDON, ACCEPT or CONTINUE
   #
   def examine() :
      raise NotImplementedError

   ## Extend the current partial solution.
   #  @return a list of extended partial solutions
   #
   def extend() :
      raise NotImplementedError

## Represent a partial solution to the 8-queens problem.
#
class EightQueensPartialSolution(PartialSolution) :
   COLUMNS = "abcdefgh"

   ## Construct a new solution to the problem.
   #
   def __init__(self, data = []) :
      super().__init__()
      self._data = data

   ## Does a queen at location p1 attack a queen at location p2.
   #  @param p1 the 2 character string describing the location of one queen
   #  @param p2 the 2 character string describing the location of a second queen
   #  @return True if they attack each other, False otherwise
   #
   def attacks(self, p1, p2) :
      column1 = self.COLUMNS.index(p1[0]) + 1
      row1 = int(p1[1])
      column2 = self.COLUMNS.index(p2[0]) + 1
      row2 = int(p2[1])
      return (row1 == row2 or column1 == column2 or
         abs(row1 - row2) == abs(column1 - column2))

   ## Examine a partial solution to see if it is acceptable, is not done, but
   #  should be continued, or should be abandoned.
   #  @return ABANDON, ACCEPT or CONTINUE
   #
   def examine(self) :
      data = self._data
      for i in range(0, len(data)) :
         for j in range(i + 1, len(data)) :
            if self.attacks(data[i], data[j]) :
               return self.ABANDON
      if len(data) == len(self.COLUMNS) :
         return self.ACCEPT
      else :
         return self.CONTINUE

   ## Extend the current partial solution by adding a new queen.
   #  @return a list of extended partial solutions
   #
   def extend(self) :
      data = self._data
      results = []
      row = len(data) + 1
      for column in self.COLUMNS :
         newSolution = EightQueensPartialSolution(data + [column + str(row)])
         results.append(newSolution)
      return results

   ## Generate a string representation of the solution.
   #  @return a string representing the solution
   #
   def __repr__(self) :
      return str(self._data)
      
## Generates all solutions to the problem that can be extended from the
#  provided partial solution.
#  @param ps the starting solution
#  @return a list of solutions that start from ps
#
def solve(ps) :
   solutions = []
   status = ps.examine()
   if status == PartialSolution.ACCEPT :
      solutions.append(ps)
   elif status != PartialSolution.ABANDON :
      for p in ps.extend() :
         solutions = solutions + solve(p)
   return solutions

# Call the main function.
main()

