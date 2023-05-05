game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player = 0


def check_win():
    global player
    for i in range(0, 2):
        if game[0][i] == game[1][i] == game[2][i] and game[0][i]:
            if game[0][i] == "x":
                player = 1
            elif game[0][i] == "o":
                player = 2

    if player == 0:
        for i in range(0, 2):
            if game[i][0] == game[i][1] == game[i][2] and game[i][0]:
                if game[i][0] == "x":
                    player = 1
                elif game[i][0] == "o":
                    player = 2

    if player == 0:
        if game[0][0] == game[1][1] == game[2][2] and game[0][0]:
            if game[0][0] == "x":
                player = 1
            elif game[0][0] == "o":
                player = 2
        elif game[0][2] == game[1][1] == game[2][0] and game[0][2]:
            if game[0][2] == "x":
                player = 1
            elif game[0][2] == "o":
                player = 2


def print_game():
    for i in range(0, 3):
        print(" ---" * 3)
        row = ""
        for j in range(0, 3):
            if game[i][j]:
                row = row + "| " + game[i][j] + " "
            else:
                row = row + "|   "
        print(row + "|")
    print(" ---" * 3)


def play_turn(p1):
    print_game()
    loc = []
    if p1:
        loc = input(
            "Player 1, Enter the row [1,3] and column [1,3] of your move in this format \"ROW,COL\": ").strip().split(
            ",")
    else:
        loc = input(
            "Player 2, Enter the row [1,3] and column [1,3] of your move in this format \"ROW,COL\": ").strip().split(
            ",")

    loc = [int(loc[0]), int(loc[1])]
    if loc[0] < 1 or loc[0] > 3 or loc[1] < 1 or loc[1] > 3:
        print("Please Enter valid row and column.")
        return play_turn(p1)
    elif game[loc[0] - 1][loc[1] - 1]:
        print("Already occupied, please try again")
        return play_turn(p1)
    elif p1:
        game[loc[0] - 1][loc[1] - 1] = 'x'
    else:
        game[loc[0] - 1][loc[1] - 1] = 'o'
    return


p1_turn = 1
turn = 0
while turn < 9:
    play_turn(p1_turn)
    p1_turn = not p1_turn
    check_win()
    if player:
        turn = 10
    turn = turn + 1

print_game()

if player == 0:
    print("No one won")
elif player == 1:
    print("Congratulations Player 1, you won!")
else:
    print("Congratulations Player 2, you won!")
