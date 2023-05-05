file = open("Day11Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]
width = len(var[0])
height = len(var)
var_int = []
for i in range(0, height):
    var_int.append([])
    for j in range(0, width):
        if var[i][j] == '#':
            var_int[i].append(1)
        elif var[i][j] == 'L':
            var_int[i].append(0)
        else: 
            var_int[i].append(-1)

def part1(a):
    b = [x[:] for x in a]
    is_done = 1
    for i in range(0, height):
        for j in range(0, width):
            if a[i][j] != -1:
                seat_occupied_num = 0
                for r in [-1, 0, 1]:
                    for c in [-1, 0, 1]:
                        if not(r == 0 and c == 0) and not(i == 0 and c == -1) and not(i == (height - 1) and c == 1) and not(j == 0 and r == -1) and not(j == (width - 1) and r == 1):
                            if a[i + c][j + r] == 1:
                                seat_occupied_num += 1
                if seat_occupied_num >= 4 and a[i][j] == 1:
                    is_done = 0
                    b[i][j] = 0
                elif seat_occupied_num == 0  and a[i][j] == 0:
                    is_done = 0
                    b[i][j] = 1
    if not is_done:
        return part1(b)
    else:
        total = 0
        for i in range(0, height):
            for j in range(0, width):
                if a[i][j] == 1:
                    total += 1
        return total

def part2(a):
    b = [x[:] for x in a]
    is_done = 1

    for i in range(0, height):
        for j in range(0, width):
            
            if a[i][j] != -1:
                seat_occupied_num = 0
                for r in [-1, 0, 1]:
                    for c in [-1, 0, 1]:
                        count = 0
                        while not(r == 0 and c == 0):
                            count += 1
                            h = i + (c*count)
                            w = j + (r*count)
                            if (0 <= h < height) and (0 <= w < width):
                                if a[h][w] == 1:
                                    seat_occupied_num += 1
                                    break
                                elif a[h][w] == 0:
                                    break
                            else: 
                                break
                
                if seat_occupied_num >= 5 and a[i][j] == 1:
                    is_done = 0
                    b[i][j] = 0
                elif seat_occupied_num == 0  and a[i][j] == 0:
                    is_done = 0
                    b[i][j] = 1

    if not is_done:
        return part2(b)
    else:
        total = 0
        for i in range(0, height):
            for j in range(0, width):
                if a[i][j] == 1:
                    total += 1
        return total

print(part2(var_int))