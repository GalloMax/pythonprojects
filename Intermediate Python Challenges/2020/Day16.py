file = open("Day16Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]

header = {}
valid_header = []
valid_temp = {}
for i in range(0, len(var)):
    if var[i] == '':
        break
    else:
        line = var[i][::].split()
        line = line[len(line) - 3::2]
        temp = []
        temp.append(int(line[0].split('-')[0]))
        temp.append(int(line[0].split('-')[1]))
        temp.append(int(line[1].split('-')[0]))
        temp.append(int(line[1].split('-')[1]))
        header[i] = temp[::]
        valid_temp[i] = True

for i in range(0, len(header)):
    valid_header.append(valid_temp.copy())

nearby = []
for i in range(len(header) + 5, len(var)):
    nearby.append([int(a) for a in var[i][::].split(',')])

invalid = {}
def part1():
    num = 0
    for i in range(0, len(nearby)):
        bad_1 = False
        for k in nearby[i]:
            bad = True
            for j in range(0, len(header)):
                temp = header[j]
                #print(f"k: {k}  temp: {temp}")
                if temp[0] <= k <= temp[1] or temp[2] <= k <= temp[3]:
                    bad = False
            if bad:
                num += k
                bad_1 = True
        if bad_1:
            invalid[i] = True
        else:
            invalid[i] = False
    return num


def part2():
    for i in range(0, len(nearby)):
        if not invalid[i]:
            for j in range(0, len(header)):
                for k in range(0, len(header)):
                    temp = header[k]
                    #print(f"k: {k}  temp: {temp}")
                    if not(temp[0] <= nearby[i][j] <= temp[1] or temp[2] <= nearby[i][j] <= temp[3]):
                        valid_header[j][k] = False
    #print(valid_header)
    count = 0
    temp = [[aa for aa in bb if bb[aa]] for bb in valid_header]
    ticket_num = {}
    # for i in range(0, len(temp)):
    #     print(f"temp[{i}]: {temp[i]}")
    while count != len(header):
        for i in range(0, len(temp)):
            if len(temp[i]) == 1:
                ticket_num[i] = temp[i][0]
                for j in range(0, len(temp)):
                    try:
                        temp[j].remove(ticket_num[i])
                    except ValueError:
                        continue
                count += 1

    print(ticket_num)

    return ""

#print(nearby)
print()
print(f"Part 1: {part1()}")
print()
print(f"Part 2: {part2()}")
print()