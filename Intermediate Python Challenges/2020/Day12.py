file = open("Day12Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]


def part1(v):
    ns = 0
    ew = 0
    direction = 90
    
    for i in v:
        direction = direction % 360
        mov = int(i[1:len(i)])
        if i[0] == 'F':
            if direction == 0:
                ns += mov
            elif direction == 90:
                ew += mov
            elif direction == 180:
                ns -= mov
            else:
                ew -= mov
        elif i[0] == 'R':
            direction += mov
        elif i[0] == 'L':
            direction -= mov
        elif i[0] == 'N':
            ns += mov
        elif i[0] == 'S':
            ns -= mov
        elif i[0] == 'E':
            ew += mov
        else:
            ew -= mov
    
    return abs(ns) + abs(ew)

def part2(v):
    ns = 0
    ew = 0
    w_ns = 1
    w_ew = 10
    
    for i in v:
        mov = int(i[1:len(i)])
        if i[0] == 'F':
            ns += w_ns * mov
            ew += w_ew * mov
        elif i[0] == 'R' or i[0] == 'L':
            if i[0] == 'L':
                mov = 360 - mov
            if mov == 90:
                temp = w_ns
                w_ns = -w_ew
                w_ew = temp
            elif mov == 270:
                temp = -w_ns
                w_ns = w_ew
                w_ew = temp
            elif mov == 180:
                w_ns = -w_ns
                w_ew = -w_ew

        elif i[0] == 'N':
            w_ns += mov
        elif i[0] == 'S':
            w_ns -= mov
        elif i[0] == 'E':
            w_ew += mov
        elif i[0] == 'W':
            w_ew -= mov    
    return abs(ns) + abs(ew)

print(part2(var))