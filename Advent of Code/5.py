lines = []
with open("5.input") as f:
    lines = [i.rstrip("\n") for i in f.readlines()]

shared = []
for i in lines:
    n = len(i) // 2
    first = i[:n]
    second = i[n:]
    shared.append(set(first) & set(second))

score = 0
for j in shared:
    i = list(j)[0]
    if ord(i) >= 97:
        score += ord(i) - 96
    else: score += ord(i) - 38

print(score)

