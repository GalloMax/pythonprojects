file = open("Day9Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]
    var[i] = int(var[i])

def is_a_pair(loc):
    for i in var[loc - 25: loc]:
        for j in var[loc - 25: loc]:
            if j != i:
                if j + i == var[loc]:
                    return True
    return False

number = 57195069

def find_set(loc):
    for i in range(0,len(var)):
        temp = var[i]
        a = [var[i]]
        j = 1
        while temp < number and (j + i) != len(var):
            temp = temp + var[i + j]
            a.append(var[i + j])
            j = j + 1
        if temp == number:
            return max(a) + min(a)


def part1():
    for i in range(25, len(var)):
        if not is_a_pair(i):
            return var[i]

def part2():
    for i in range(25, len(var)):
        if not is_a_pair(i):
            return find_set(i)

print(part2())