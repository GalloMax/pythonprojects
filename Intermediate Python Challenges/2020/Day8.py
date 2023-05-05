file = open("Day8Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]

def get_a_part1(v):
    loc = 0
    a = 0
    while loc != len(v) and v[loc]:
        temp = loc

        if v[loc][0:3] == "nop":
            loc = loc + 1
        elif v[loc][0:3] == "acc":
            a = a + int(v[loc][4:len(v[loc])])
            loc = loc + 1
        else:
            loc = loc + int(v[loc][4:len(v[loc])])
        v[temp] = 0
    return a

def will_end(v):
    loc = 0
    a = 0
    while True:
        if loc != len(v) and v[loc]:
            temp = loc

            if v[loc][0:3] == "nop":
                loc = loc + 1
            elif v[loc][0:3] == "acc":
                a = a + int(v[loc][4:len(v[loc])])
                loc = loc + 1
            else:
                loc = loc + int(v[loc][4:len(v[loc])])
            v[temp] = 0
        elif loc == len(v):
            return True
        else:
            return False


def get_a_part2(v):
    loc = 0
    a = 0
    while v[loc]:
        temp = loc
        if v[loc][0:3] == "nop":
            tempv = var.copy()
            tempv[loc] = "jmp" + tempv[loc][3:len(tempv[loc])]
            print(tempv[loc])
            print(v[loc])
            if will_end(tempv):

                var[loc] = "jmp" + var[loc][3:len(var[loc])]
                return get_a_part1(var)
            loc = loc + 1
        elif v[loc][0:3] == "acc":
            a = a + int(v[loc][4:len(v[loc])])
            loc = loc + 1
        else:
            tempv = var.copy()
            tempv[loc] = "nop" + tempv[loc][3:len(tempv[loc])]
            if will_end(tempv):
                print(var[loc])
                var[loc] = "nop" + var[loc][3:len(var[loc])]
                return get_a_part1(var)
            loc = loc + int(v[loc][4:len(v[loc])])
        v[temp] = 0
    return a
    
tempvar = var.copy()
print(get_a_part2(tempvar))
