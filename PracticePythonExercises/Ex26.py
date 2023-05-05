game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def play_turn(p1):
    print(game)
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
while True:
    play_turn(p1_turn)
    p1_turn = not p1_turn
