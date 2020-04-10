from random import randint

board = []

print "1.-- Your mission is to find the 1x1 ship"
print "\n2.-- You have only 5 Turns"
print "\n3.-- the coordinate system starts with 0 and ends with 2.( so the upper left corner coordinate is row 0, col 0"
print"\n4.-- Your previous Turns will be marked with an X, otherwise you get a message if you hit the ship or shot outside the coordinate system"
print "\n5.-- Good luck!\n"
for x in range(0, 3):
  board.append(["O"] * 3)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)



# Everything from here on should be in your for loop

for turn in range(10):
  print "Turn", turn + 1,"/5"
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "\nCongratulations! You sank my battleship!"
    break
  else:
    if guess_row not in range(3) or \
      guess_col not in range(3):
      print "\nOops, that's not even in the ocean.\n"
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "\nYou missed my battleship!"
      board[guess_row][guess_col] = "X"
    if turn == 4:
      print "\nThe ship was located in:"
      print "row:",ship_row
      print "col:",ship_col
      print "\nGame Over"
      break
    print_board(board)
