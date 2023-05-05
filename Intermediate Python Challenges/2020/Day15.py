var = [14,1,17,0,3,20]

def part1(v):
    latest = {}
    pre_latest = {}
    last = v[len(v) - 1]
    for i in range(0, len(v)):
        latest[v[i]] = i + 1
    #print(f"Latest: {latest}")
    #print(f"Pre-Latest: {pre_latest}")
    for i in range(len(v) + 1, 30000001):
        #print(f"i: {i}  Latest: {latest}  Pre-Latest: {pre_latest}  Last: {last}")
        if last in pre_latest:
            last = latest[last] - pre_latest[last]
            if last in latest:
                pre_latest[last] = latest[last]
            latest[last] = i
        else:
            last = 0
            pre_latest[last] = latest[last]
            latest[last] = i


    return last

print(f"Part 1: {part1(var.copy())}")
            
    