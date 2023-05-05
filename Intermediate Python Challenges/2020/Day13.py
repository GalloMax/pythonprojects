file = open("Day13Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]

def part1(v):
    a = v[1].split(',')
    b = int(v[0])
    a = [int(xx) for xx in a if xx != "x"]
    min = 10000000
    min_bus = 0
    for i in a:
        if (i - (b % i)) < min:
            min = (i - (b % i))
            min_bus = i
    return min * min_bus


def part2(v):
    a = v[1].split(',')
    l = len(a) - 1
    done = False
    d = {}
    for i in range(0, len(a)):
        if a[i] != "x":
            b = int(a[i])
            d[b] = i
    a = [int(xx) for xx in a if xx != "x"]
    m = max(a)
    m_i = d[m]
    time = m
    while not done:
        done = True
        for i in a:
            if (time - (m_i - d[i])) % i:
                done = False
                continue
        time += m

    return time - m - m_i

print(f"Part 1: {part1(var.copy())}")
print(f"Part 2: {part2(var.copy())}")