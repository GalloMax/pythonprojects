file = open("Day10Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]
    var[i] = int(var[i])


def part1(v):
    one = 0
    three = 0
    n = 0
    while len(v):
        m = min(v)
        if m - n == 1:
            one = one + 1
        elif m - n == 3:
            three = three + 1
        n = m
        v.remove(n)

    three = three + 1

    return three * one

def part2(array, len):
    possibilities = []
    for i in range(0, len):
        possibilities.append(1)
    if array[1] - array[0] < 4:
        possibilities[2] = possibilities[0] + possibilities[1]
    for i in range(3, len):
        possibilities[i] = possibilities[i - 1]
        if(array[i] - array[i - 2] < 4):
            possibilities[i] += possibilities[i - 2]
            if(array[i] - array[i - 3] == 3):
                possibilities[i] += possibilities[i - 3]
    return possibilities[len - 1]



var.append(0)
var = sorted(var)
print("part2: " + str(part2(var, len(var))))