##
#  Find a path out of a maze.
#

MAZE = ["*********", 
         "*     * *", 
         "* ***** *", 
         "* * *   *", 
         "* * *** *", 
         "*   *   *", 
         "*** * * *", 
         "      * *", 
         "*********"]

def main() :
   # Try to escape from a maze, reporting the escape path.
   path = []
   success = canEscape(MAZE, 3, 1, path)
   if success :
      print("You can escape from the maze by following this path:")
      print(path)
   else :
      print("There is no escape.")

## Determine if one can escape from a maze, starting at (row, col).
#  @param maze the maze that one is trying to escape from
#  @param row the starting row
#  @param col the starting column
#  @param p a list that accumulates the escape path (should be empty when the function is called for the first time
#  @return True if one can escape from the maze, False otherwise
#
def canEscape(maze, row, col, p) :
   # If (row, col) is in p then we are trying to pass through a prohibited 
   # space, so we must return False.
   if (row, col) in p :
      return False

   # If we are at an escape point.
   if row == 0 or row == len(maze) - 1 or \
      col == 0 or col == len(maze[row]) - 1 :
      p.append((row, col))
      return True
   
   # Assume that we won't find the exit until we prove otherwise.
   done = False

   # Try to escape by going up.
   if row - 1 >= 0 and maze[row - 1][col] == " " :
      p.append((row, col))
      done = done or canEscape(maze, row - 1, col, p)
      if not done :
         p.pop()
   
   # Try to escape by going down.
   if not done and row + 1 < len(maze) and maze[row + 1][col] == " " :
      p.append((row, col))
      done = done or canEscape(maze, row + 1, col, p)
      if not done :
         p.pop()

   # Try to escape by going left.
   if not done and col - 1 >= 0 and maze[row][col - 1] == " " :
      p.append((row, col))
      done = done or canEscape(maze, row, col - 1, p)
      if not done :
         p.pop()

   # Try to escape by going right.
   if not done and col + 1 < len(maze[row]) and maze[row][col + 1] == " " :
      p.append((row, col))
      done = done or canEscape(maze, row, col + 1, p)
      if not done :
         p.pop()

   # Return the result.
   return done

# Call the main function.
main()

