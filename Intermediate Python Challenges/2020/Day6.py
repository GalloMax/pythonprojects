file1 = open("Day6Input.txt", "r")
var = []
line = file1.readline()
valid_num = 0
d = {"a": 0,
     "b": 1,
     "c": 2,
     "d": 3,
     "e": 4,
     "f": 5,
     "g": 6,
     "h": 7,
     "i": 8,
     "j": 9,
     "k": 10,
     "l": 11,
     "m": 12,
     "n": 13,
     "o": 14,
     "p": 15,
     "q": 16,
     "r": 17,
     "s": 18,
     "t": 19,
     "u": 20,
     "v": 21,
     "w": 22,
     "x": 23,
     "y": 24,
     "z": 25}


def count_yes(v):
    n = 0
    for m in v:
        if m:
            n = n + 1
    return n


num = 0
while line:
    if line.split("\n")[0]:
        if len(var) == num:
            var.append(line.split("\n")[0])
        else:
            var[num] = var[num] + " " + line.split("\n")[0]
    else:
        num = num + 1
    line = file1.readline()

for i in var:
    answers = []
    for j in range(0, 26):
        answers.append(0)
    group = i.split()
    print(group)
    for j in group:
        for k in j:
            answers[d[k]] = answers[d[k]] + 1

    for j in answers:
        if j == len(group):
            valid_num = valid_num + 1

file.close();

print(valid_num)