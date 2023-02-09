##
#  Solve the 8-Queens problem using backtracking.
#

def main() :
   # Find all of the solutions to the 8 queens problem.
   eq = EightQueensPartialSolution()
   sols = solve(eq)
   removeReflectionsRotations(sols)

   # Remove all of the reflections and rotations marked for removal.
   while None in sols :
      sols.remove(None)

   # Save the results in out.html.
   print("Writing the results to out.html")
   outf = open("out.html", "w")
   for s in sols:
      outf.write(s.toHTML())
   outf.close()

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

   def toHTML(self) :
      retval = "<table border=1 cellspacing=0 cellpading=0>\n"
      for row in range(8, 0, -1) :
         retval = retval + " <tr>\n"
         for col in self.COLUMNS: 
            if (row + ord(col)) % 2 == 0 :
               color = "#808080"
            else :
               color = "#ffffff"

            retval = retval + "<td bgcolor=\"" + color + "\">"
            if col + str(row) in self._data :
               retval = retval + "&#x2655;"
            retval = retval + "</td> "
            
         retval = retval + " </tr>\n"
            
      retval = retval + "</table>\n"
      retval = retval + "<br><br>\n\n"
      return retval

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


   ## Determine if self is a horizontal reflection of other.
   #  @param other the other solution to check
   #  @return True if it is, False otherwise
   #
   def isHReflect(self, other) :
      temp = list(other._data)
      for i in range(0, len(temp)) :
         temp[i] = chr(7 + ord("a") - ord(temp[i][0]) + ord("a")) + temp[i][1]
      if sorted(temp) == sorted(self._data) :
         return True
      return False

   ## Determine if self is a vertical reflection of other.
   #  @param other the other solution to check
   #  @return True if it is, False otherwise
   #
   def isVReflect(self, other) :
      temp = list(other._data)
      for i in range(0, len(temp)) :
         temp[i] = temp[i][0] + str(9 - int(temp[i][1]))
      if sorted(temp) == sorted(self._data) :
         return True
      return False

   ## Determine if self is a reflection of other in the positive diagonal.
   #  @param other the other solution to check
   #  @return True if it is, False otherwise
   #
   def isReflectDiag(self, other) :
      temp = list(other._data)
      for i in range(0, len(temp)) :
         old_col = ord(temp[i][0]) - ord("a") + 1
         old_row = int(temp[i][1])

         new_row = old_col
         new_col = old_row

         temp[i] = chr(ord("a") - 1 + new_col) + str(new_row)

      if sorted(temp) == sorted(self._data) :
         return True
      return False

   ## Determine if self is a reflection of other in the negative diagonal.
   #  @param other the other solution to check
   #  @return True if it is, False otherwise
   #
   def isReflectNegDiag(self, other) :
      temp = list(other._data)
      for i in range(0, len(temp)) :
         old_col = ord(temp[i][0]) - ord("a") + 1
         old_row = int(temp[i][1])

         new_row = 9 - old_col
         new_col = 9 - old_row

         temp[i] = chr(ord("a") - 1 + new_col) + str(new_row)

      if sorted(temp) == sorted(self._data) :
         return True
      return False

   ## Determine if self is a 180 degree rotation of other.
   #  @param other the other solution to check
   #  @return True if it is, False otherwise
   #
   def isRotate180(self, other) :
      temp = list(other._data)
      for i in range(0, len(temp)) :
         temp[i] = chr(7 + ord("a") - ord(temp[i][0]) + ord("a")) + temp[i][1]
         temp[i] = temp[i][0] + str(9 - int(temp[i][1]))
      if sorted(temp) == sorted(self._data) :
         return True
      return False

   ## Determine if self is a 90 degree rotation of other.
   #  @param other the other solution to check
   #  @return True if it is, False otherwise
   #
   def isRot90(self, other) :
      temp = list(other._data)
      for i in range(0, len(temp)) :
         old_col = ord(temp[i][0]) - ord("a") + 1
         old_row = int(temp[i][1])

         new_row = 9 - old_col
         new_col = old_row

         temp[i] = chr(ord("a") - 1 + new_col) + str(new_row)

      if sorted(temp) == sorted(self._data) :
         return True
      return False

   ## Determine if self is a 270 degree rotation of other.
   #  @param other the other solution to check
   #  @return True if it is, False otherwise
   #
   def isRot270(self, other) :
      temp = list(other._data)
      for i in range(0, len(temp)) :
         old_col = ord(temp[i][0]) - ord("a") + 1
         old_row = int(temp[i][1])

         new_row = old_col
         new_col = 9 - old_row

         temp[i] = chr(ord("a") - 1 + new_col) + str(new_row)

      if sorted(temp) == sorted(self._data) :
         return True
      return False

## Remove all of the reflections and rotations for a list of boards.
#  @param the list to process
def removeReflectionsRotations(data) :
   for i in range(len(data)) :
      for j in range(i + 1, len(data)) :
         if data[i] != None and data[j] != None and  \
            (data[i].isHReflect(data[j]) or \
            data[i].isVReflect(data[j]) or \
            data[i].isRotate180(data[j]) or \
            data[i].isReflectDiag(data[j]) or \
            data[i].isReflectNegDiag(data[j]) or \
            data[i].isRot90(data[j]) or \
            data[i].isRot270(data[j])) :
            data[i] = None
      
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

