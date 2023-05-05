file = open("Day5Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]


max = 0
possible = []
upper_bound = 127
lower_bound = 0
r = range(48, 819)
for i in range(0, len(var)):
    upper_bound = 127
    lower_bound = 0
    for j in range(0, 7):
        if var[i][j] == "B":
            lower_bound = lower_bound + 2**(6-j)
        else:
            upper_bound = upper_bound - 2**(6-j)

    temp = lower_bound * 8

    lower_bound = 0
    upper_bound = 7

    for j in range(7, 10):
        if var[i][j] == "R":
            lower_bound = lower_bound + 2**(9 - j)
        else:
            upper_bound = upper_bound + 2**(9 - j)

    temp = temp + lower_bound
    possible.append(temp)

for i in r:
    if i not in possible:
        print(i)

print(sorted(possible))
print(len(possible))
print(len(var))
print(len(r))

