##
#  Solve a maze using backtracking.
#

def main() :
   MAZE =  ["* *******", 
            "*     *  ", 
            "* ***** *", 
            "* * *   *", 
            "* * *** *", 
            "*   *   *", 
            "*** * * *", 
            "      * *", 
            "******* *"]

   # Find all of the solutions to maze.
   eq = MazePartialSolution(MAZE, 3, 1)
   sols = solve(eq)
   for s in sols:
      print("Walk this way:", s)

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

## Represent a partial solution to the maze problem.
#
class MazePartialSolution(PartialSolution) :
   START = 0
   SEARCHING = 1

   ## Construct a new solution to the problem.
   #  @param maze the maze to solve
   #  @param row the starting row in the maze
   #  @param col the starting column in the maze
   #  @param p the list of prohibited squares that we can't pass through
   #
   def __init__(self, maze, row, col, p = []) :
      super().__init__()
      self._maze = maze
      self._row = row
      self._col = col
      self._p = p + [(row, col)]

   ## Examine a partial solution to see if it is acceptable, is not done, but
   #  should be continued, or should be abandoned.
   #  @return ABANDON, ACCEPT or CONTINUE
   #
   def examine(self) :
      if len(self._p) == 0 :
         return self.ABANDON

      lastrow = self._p[-1][0]
      lastcol = self._p[-1][1]

      if lastrow == 0 or \
         lastcol == 0 or \
         lastrow == len(self._maze) - 1 or \
         lastcol == len(self._maze[lastrow]) - 1 :
         return self.ACCEPT

      return self.CONTINUE

   ## Extend the current partial solution by moving in the legal directions.
   #  @return a list of extended partial solutions
   #
   def extend(self) :
      results = []

      lastrow = self._p[-1][0]
      lastcol = self._p[-1][1]

      for (rowchg, colchg) in [(0, -1), (0, 1), (-1, 0), (1, 0)] :
         newrow = lastrow + rowchg
         newcol = lastcol + colchg
         if self._maze[newrow][newcol] == " " and (newrow, newcol) not in self._p:
            nextSol = MazePartialSolution(self._maze, newrow, newcol, self._p)
            results.append(nextSol)

      return results

   ## Generate a string representation of the solution.
   #  @return a string representing the solution
   #
   def __repr__(self) :
      return str(self._p)
      
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

