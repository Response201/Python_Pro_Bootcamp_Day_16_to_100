import time


board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
keep_playing = True
round_number = 1
player ="X"
print(f"Player X's turn, round {round_number}/9")




def draw_board(board):
   display_board = ""

   for item in range(len(board)):

       if (item + 1) % 3 == 0:
           display_board += f"{board[item]} \n"
       elif (item - 1) % 3 == 0:
           display_board += f" | {board[item]} | "
       else:
           display_board += f"{board[item]}"

   print(f"\n{display_board}")

draw_board(board)



def place_marker(spot, player):

    if board[spot] != "X" and board[spot] != "O":
        board[spot] = player
        return True

    return False



def player_pick_spot():
    try:
        spot = int(input(f"Pick a number 1-9\n")) - 1

        if spot >= 0 and spot <= 8:
            return spot
        else:
            print("Invalid position")
            return None

    except ValueError:
       print("Invalid input")
       return None



def new_round(round,player, keep_playing):
    if round <= 8:
        round += 1
        player = "O" if round % 2 == 0 else "X"
        print(f"Player {player}'s turn, round {round}/9")
        return round, player, keep_playing
    else:
        keep_playing = False
        print("Game over")
        return round, player, keep_playing



def winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for item in winning_combinations:
        if board[item[0]] == board[item[1]] == board[item[2]]:
            return True

    return False




while keep_playing:

        spot = player_pick_spot()
        if spot is not None:
            if place_marker(spot, player):
                time.sleep(0.2)
                print('\n' * 33)
                draw_board(board)
                if not winner():
                    round_number, player, keep_playing = new_round(round_number, player, keep_playing)
                else:
                    print(f"{player} is the winner")
                    keep_playing = False

            else:
                print("Spot already taken")



