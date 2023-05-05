file = open("Day17Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]
side = len(var)
possible_side = side + 10
bottom = -possible_side//2 + 1
top = possible_side//2 + 1

#print()
# for i in var:
#     print(i)

g = {}
for x in range(bottom, top):
    g[x] = {}
    for y in range(bottom, top):
        g[x][y] = {}
        for z in range(bottom, top):
            g[x][y][z] = '.'
g = [[[g[xx][yy][zz] for zz in g[xx][yy]] for yy in g[xx]] for xx in g]
for x in range(-side//2 + 1, side//2 + 1):
    for y in range(-side//2 + 1, side//2 + 1):
        g[x][y][0] = var[x + (side - 1)//2][y + (side - 1)//2]

def p(c):
    for z in range(bottom, top):
        print()
        print(f"z: {z}")
        for x in range(bottom, top):
            temp = ""
            for y in range(bottom, top):
                temp += c[x][y][z]
            print(temp)
    return

# for i in range(bottom, top):
#     print(i)
#     for j in range(bottom, top):
#         print(" ", j)
#         print("   ", g[i][j])

#p(g)

def part1(side, b):
    a = [[aa.copy() for aa in bb].copy() for bb in b.copy()]
    for i in range(0, 6):
        #if i == 2:
            #p(a)
        for x in range(bottom, top):
            for y in range(bottom, top):
                for z in range(bottom, top):
                    num_active = 0
                    for x_d in [-1, 0, 1]:
                        for y_d in [-1, 0, 1]:
                            for z_d in [-1, 0, 1]:
                                if x_d or y_d or z_d:
                                    if b[x + x_d][y + y_d][z + z_d] == '#':
                                        num_active += 1
                    if (2 <= num_active <= 3) and (b[x][y][z] == '#'):
                         continue
                    elif num_active == 3 and b[x][y][z] == '.':
                        a[x][y][z] = '#'
                    else:
                        a[x][y][z] = '.'
        b = [[aa.copy() for aa in bb] for bb in a.copy()]
    total = 0
    for x in range(bottom, top):
        for y in range(bottom, top):
            for z in range(bottom, top):
                if b[x][y][z] == '#':
                    total += 1
    return total


d = {}
for x in range(bottom, top):
    d[x] = {}
    for y in range(bottom, top):
        d[x][y] = {}
        for z in range(bottom, top):
            d[x][y][z] = {}
            for w in range(bottom, top):
                d[x][y][z][w] = '.'
d = [[[[d[xx][yy][zz][ww] for ww in d[xx][yy][zz]] for zz in d[xx][yy]] for yy in d[xx]] for xx in d]
for x in range(-side//2 + 1, side//2 + 1):
    for y in range(-side//2 + 1, side//2 + 1):
        d[x][y][0][0] = var[x + (side - 1)//2][y + (side - 1)//2]


def part2(side, b):
    a = [[[ii.copy() for ii in aa].copy() for aa in bb].copy() for bb in b.copy()]
    for i in range(0, 6):
        #if i == 2:
            #p(a)
        for x in range(bottom, top):
            for y in range(bottom, top):
                for z in range(bottom, top):
                    for w in range(bottom, top):
                        num_active = 0
                        for x_d in [-1, 0, 1]:
                            for y_d in [-1, 0, 1]:
                                for z_d in [-1, 0, 1]:
                                    for w_d in [-1, 0, 1]:
                                        if x_d or y_d or z_d or w_d:
                                            if b[x + x_d][y + y_d][z + z_d][w + w_d] == '#':
                                                num_active += 1
                        if (2 <= num_active <= 3) and (b[x][y][z][w] == '#'):
                             continue
                        elif num_active == 3 and b[x][y][z][w] == '.':
                            a[x][y][z][w] = '#'
                        else:
                            a[x][y][z][w] = '.'
        b = [[[ii.copy() for ii in aa].copy() for aa in bb].copy() for bb in a.copy()]
    total = 0
    for x in range(bottom, top):
        for y in range(bottom, top):
            for z in range(bottom, top):
                for w in range(bottom, top):
                    if b[x][y][z][w] == '#':
                        total += 1
    return total


print()
print(f"Part 1: {part1(side, g.copy())}")
print()
print(f"Part 2: {part2(side, d.copy())}")
print()