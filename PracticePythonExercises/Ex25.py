game = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]

player = 0
for i in range(0, 2):
    if game[0][i] == game[1][i] == game[2][i] and game[0][i]:
        player = game[0][i]

if player == 0:
    for i in range(0, 2):
        if game[i][0] == game[i][1] == game[i][2] and game[i][0]:
            player = game[i][0]

if player == 0:
    if game[0][0] == game[1][1] == game[2][2] and game[0][0]:
        player = game[0][0]
    elif game[0][2] == game[1][1] == game[2][0] and game[0][2]:
        player = game[0][2]

print(player)
