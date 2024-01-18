# ----------------------------------------------------------
# ----------------- PRE-DEFINED FUNCTIONS ------------------
# ----------------------------------------------------------

def print_tictactoe(values):
  # Prints the 3 x 3 grid for Tic-Tac-Toe, given a list of 
  # 9 strings consisting of "O", "X", or a string 
  # with an empty space.  
  
  print("\n")
  print("     |     |     ")
  print("  {}  |  {}  |  {} ".format(values[0], values[1], values[2]))
  print("_____|_____|_____")
  print("     |     |     ")
  print("  {}  |  {}  |  {} ".format(values[3], values[4], values[5]))
  print("_____|_____|_____")
  print("     |     |     ")
  print("  {}  |  {}  |  {} ".format(values[6], values[7], values[8]))
  print("     |     |     ")

def twoplayer_setup():
  # Sets up the game for two players, letting players choose
  # what icon to use.
  print("You are about to play Tic-Tac-Toe with 2 players.")
  while True:
    player1 = input("Player 1, please type O or X: ").upper()
    if player1 == "O":
      print("Player 1 has chosen O.")
      player2 = "X"
      print("Player 2 is assigned X.")
      break
    elif player1 == "X":
      print("Player 1 has chosen X.")
      player2 = "O"
      print("Player 2 is assigned O.")
      break
    else:
      print("Player 1 can only choose O or X. Try again.")
  print("Player 1 will go first.")
  return {"Player 1": player1, "Player 2": player2}

def grid_reference():
  # Prints the grid sections numbered 1-9.
  print("To refer to a section of the grid, please see this diagram.")
  print_tictactoe(range(1, 10))

def playerturn(player_icon, values):
  # Changes one of the sections on the grid to the player's icon.
  while True:
    try:
      player_input = int(input(f"Select which section of the grid to input {player_icon} into: "))
    except ValueError:
      print("Your inputted value needs to be an integer.")
    if player_input < 1 or player_input > 9:
      print("Your inputted value needs to be between 1 to 9 inclusive.")
    else:
      n = player_input - 1
      if values[n] == " ":
        values[n] = player_icon
        break
      else:
        print("There is already an input in this section of the grid. Try again.")
  print_tictactoe(values)

def winning_setup(player_icon, values):
  # Indicator of when a player has won. Returns True if the match is won.
  # There are 4 ways a player can win; a horizontal match, a vertical match, 
  # a forwards diagonal match (ie. like a forwardslash /), and the backwards
  # diagonal match (similar to a backslash \).
  # We start by checking horizontal matches.
  for i in range(0, 9, 3):
    if (values[i] and values[i + 1] and values[i + 2])== player_icon:
      return "horizontal match"
  # We check for vertical matches.
  for j in range(3):
    if (values[j] and values[j + 3] and values[j + 6])== player_icon:
      return "vertical match"
  # We check for backwards diagonal matches.
  if (values[0] and values[4] and values[8]) == player_icon:
    return "backward diagonal match"
  # We check for forwards diagonal matches.
  if (values[2] and values[4] and values[6]) == player_icon:
    return "forward diagonal match"

def draw_setup(values):
  # Tests for a draw in the game, which occurs if the grid is full,
  # and if there are no winning matches for both players.
  full_grid = True
  for i in range(9):
    if values[i] == " ":
      full_grid = False
  if (winning_setup("O", values) and winning_setup("X", values)) == None and full_grid == True:
    return True

# ----------------------------------------------------------
# -------------------- MAIN CODE ---------------------------
# ----------------------------------------------------------

# We firstly set up the player icons.
player_dict = twoplayer_setup()

# The players list aids in referring to player_dict 
# and alternating between players more effectively on their turn.
players = ["Player 1", "Player 2"]
player_turn_count = 0

# We show the players how to refer to a section of the grid.
grid_reference()

# The list grid_values holds the data for the game.
grid_values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

while True:
  # The variable j aids in alternating between players' turns.
  j = player_turn_count % 2
  player_active = players[j]
  # Active player phase starts.
  print(f"{player_active}'s turn.")
  playerturn(player_dict[player_active], grid_values)
  # Winning branch is here.
  if winning_setup(player_dict[player_active], grid_values):
    print(f"{player_active} won!")
  # Draw branch is here
  elif draw_setup(grid_values):
    print("The game ends in a draw!")
    break
  else:
    player_turn_count += 1
