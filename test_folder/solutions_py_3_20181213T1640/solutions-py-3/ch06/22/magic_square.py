##
#  Create an n x n magic square.
#

# Read the board size from the user.
n = int(input("Enter an odd integer: "))

# Create an empty board.
board = []
for row in range(0, n) :
   board.append([0] * n)

# Populate the board.
row = n - 1
col = n // 2
for k in range(1, n * n + 1) :
   board[row][col] = k
   old_row = row
   old_col = col
   row = (row + 1) % n
   col = (col + 1) % n
   if board[row][col] != 0 :
      row = old_row
      col = old_col
      row = row - 1

# Display the board.
for row in range(0, n) :
   for col in range(0, n) :
      print("%3d" % board[row][col], end="")
   print()
   

