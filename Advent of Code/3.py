lines = []
p1 = []
p2 = []
with open("3.input") as f:
    lines = [i.rstrip("\n") for i in f.readlines()]
    p1 = [i[0] for i in lines]
    p2 = [i[2] for i in lines]

# Y beats A, ties with B, loses to C, playing it gives you 2
scoring = {
    'Y' : ['A', 'B', 2],
    'X' : ['C', 'A', 1],
    'Z' : ['B', 'C', 3]
}

score = 0
for i, p2_play in enumerate(p2):
    p1_play = p1[i]
    score += scoring[p2_play][2]

    if p1_play == scoring[p2_play][0]:
        score += 6
    elif p1_play == scoring[p2_play][1]:
        score += 3

print(score)
        
