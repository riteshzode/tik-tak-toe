import random

print("welcome to the game")

possible_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def show_board():
    for row in board:
        print(" | ".join(row))
    print()


def player_choice(number, turn):
    row, col = (number - 1) // 3, (number - 1) % 3
    board[row][col] = turn


# def player_choice(number, turn):
#     number -= 1
#     if number == 0:
#         board[0][0] = turn
#     elif number == 1:
#         board[0][1] = turn
#     elif number == 2:
#         board[0][2] = turn
#     elif number == 3:
#         board[1][0] = turn
#     elif number == 4:
#         board[1][1] = turn
#     elif number == 5:
#         board[1][2] = turn
#     elif number == 6:
#         board[2][0] = turn
#     elif number == 7:
#         board[2][1] = turn
#     elif number == 8:
#         board[2][2] = turn


def check_winner(board):
    # check row
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != "_":
        print(f"The Winner is {board[0][0]}")
        return True

    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != "_":
        print(f"The Winner is {board[1][0]}")

    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != "_":
        print(f"The Winner is {board[2][0]}")

    # check column
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != "_":
        print(f"The Winner is {board[0][0]}")
        return True

    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != "_":
        print(f"The Winner is {board[1][0]}")

    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != "_":
        print(f"The Winner is {board[2][0]}")

    # check Diagonal

    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        print(f"The Winner is {board[1][0]}")

    elif board[2][0] == board[1][1] == board[0][2] and board[2][0] != "_":
        print(f"The Winner is {board[2][0]}")


counter = 0
winner = None
tie_match = None
show_board()

while counter < 9:
    winner = check_winner(board)  # winner == True
    if winner:
        break


    if counter % 2 == 0:
        # show_board()
        user_input = int(input("Enter the Position: "))

        # if user_input >= 1 and user_input <= 9:
        if user_input in possible_number:
            player_choice(number=user_input, turn="X")
            possible_number.remove(user_input)
            show_board()

        else:
            print("slot already taken")
        # else:
        #     print("wrong answer")
        counter += 1

    else:
        while True:
            computer_choice = random.choice(possible_number)
            print(f"Computer choice is {computer_choice}")

            if computer_choice in possible_number:
                player_choice(number=computer_choice, turn="O")
                possible_number.remove(computer_choice)
                counter += 1
                show_board()

                break
            show_board()
print("Match Tie")
