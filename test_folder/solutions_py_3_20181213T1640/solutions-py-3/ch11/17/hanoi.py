##
#  Simulate the Towers of Hanoi.
#
BEFORE_LARGEST = 0
LARGEST = 1
AFTER_LARGEST = 2
DONE = 3

## Move disks for the Towers of Hanoi problem.
#
class DiskMover() :
   ## Create a new disk mover for a number of disks.
   #  @param num the number of disks
   #  @param source the source peg (1, 2 or 3)
   #  @param desk the destination peg (1, 2 or 3, different from source)
   #
   def __init__(self, num, source, dest) :
      self._n = num
      self._source = source
      self._dest = dest

      # If the number of disks is 0 we are already done.
      if num == 0:
         self._state = DONE
      # If the number of disks is greater than 1 then we need to move n - 1
      # disks to the other peg, move the bottom disk, and then move n - 1
      # disks from the other peg to the destination.
      elif num > 1 :
         self._state = BEFORE_LARGEST
         self._restIterator = DiskMover(num - 1, source, 6 - source - dest)
      # There is only 1 disk to move.
      else :
         self._state = LARGEST
         self._restIterator = None

   ## Determine if there are more moves to make.
   #  @return True is there are still more moves, False otherwise
   #
   def hasMoreMoves(self) :
      return self._state != DONE
      
   ## Make the next move.
   #  @return a string describing the move
   #
   def nextMove(self) :
      # Handle moving n - 1 disks from the source peg to the other peg.
      if self._state == BEFORE_LARGEST :
         if not self._restIterator.hasMoreMoves() :
            self._state = LARGEST
         else :
            return self._restIterator.nextMove()

      # Move the largest peg from the source peg to the destination peg.
      if self._state == LARGEST :
         retval = "Move disk from peg %d to %d" % (self._source, self._dest)
         if self._n - 1 > 0 :
            self._state = AFTER_LARGEST
            self._restIterator = DiskMover(self._n - 1, 6 - self._source - self._dest, self._dest)
         else :
            self._state = DONE
         return retval

      # Move n - 1 disks from the other peg to the destination peg.
      if self._state == AFTER_LARGEST :
         if self._restIterator.hasMoreMoves() :
            retval = self._restIterator.nextMove()
            if not self._restIterator.hasMoreMoves() :
               self._state = DONE
            return retval
         self._state = DONE

def main() :
   # Demonstrate the DiskMover class.
   mover = DiskMover(5, 1, 3)
   while mover.hasMoreMoves() :
      print(mover.nextMove())

# Call the main function.
main()

