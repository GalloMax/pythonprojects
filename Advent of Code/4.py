lines = []
p1 = []
p2 = []
with open("3.input") as f:
    lines = [i.rstrip("\n") for i in f.readlines()]
    p1 = [i[0] for i in lines]
    p2 = [i[2] for i in lines]

# Y beats A, ties with B, loses to C, playing it gives you 2
scoring = {
    'Y' : [('A', 1), ('B', 2), ('C', 3), 3],
    'X' : [('A', 3), ('B', 1), ('C', 2), 0],
    'Z' : [('A', 2), ('B', 3), ('C', 1), 6],
}

score = 0
for i, p2_play in enumerate(p2):
    p1_play = p1[i]
    score += scoring[p2_play][3]

    if p1_play == scoring[p2_play][0][0]:
        score += scoring[p2_play][0][1]
    elif p1_play == scoring[p2_play][1][0]:
        score += scoring[p2_play][1][1]
    elif p1_play == scoring[p2_play][2][0]:
        score += scoring[p2_play][2][1]
    
    print(p1_play, p2_play, score)

print(score)
        
