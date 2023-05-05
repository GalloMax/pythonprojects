file = open("Day18Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]

def p1_calc(s):
    left = ""
    index = 0
    if s[0] == '(':
        p = 1
        while p != 0:
            index += 1
            #print(f"s: {s}  index: {index}")
            if s[index] == ')':
                p -= 1
            elif s[index] == '(':
                p += 1
        if index == len(s) - 1:
            return p1_calc(s[1:len(s) - 1])
        else:
            left = str(p1_calc(s[1:index]))
            index += 1
    while index != len(s) and s[index] != "*" and s[index] != "+":
        left += s[index]
        index += 1
    left = int(left)
    if index == len(s):
        return left
    elif s[index] == "*":
        return left * p1_calc(s[index + 2::])
    else:
        return left + p1_calc(s[index + 2::])



def part1(v):
    num = 0
    for i in v:
        temp = ""
        for j in i.split()[::-1]:
            if j[len(j) - 1] == ')':
                while j[len(j) - 1] == ')':
                    #print(" hellow")
                    #print(f"  {j[0:len(j) - 1]}")
                    j = '(' + j[0:len(j) - 1]
                    #print(j)
            elif j[0] == '(':
                while j[0] == '(':
                    j = j[1:len(j)] + ')'
            temp += j + " "
        #print(temp)
        num += p1_calc(temp[0:len(temp) - 1])
    return num




def p2_calc(s):
   
    p = 0
    if '(' in s:
        #print(f"s: {s} has brackets")
        for i in range(len(s)):
            if s[i] == '(':
                p = i
            elif s[i] == ')':
                #print(f"s[0:p]:{s[0:p]}|s[p + 1:i]:{s[p + 1:i]}|s[i + 1::]:{s[i + 1::]}|")
                s = s[0:p] + str(p2_calc(s[p + 1:i])) + s[i + 1::]
                return p2_calc(s)

    if '+' in s:
        #print(f"s: {s} has a plus sign")
        left = ""
        right = ""
        index_l = 0
        index_r = 0
        for i in range(0, len(s)):
            if s[i] == '+':
                #print(f"s[{i}] is a plus")
                index_l = i - 2
                index_r = i + 2
                while index_l >= 0 and s[index_l] != " ":
                    left = s[index_l] + left
                    index_l -= 1
                while index_r < len(s) and s[index_r] != " ":
                    right = right + s[index_r]
                    index_r += 1
                break
        #print(f"s: {s}  left: {left}  right: {right}")
        s = s[0:index_l + 1] + str(p1_calc(s[index_l + 1: index_r])) + s[index_r::]
        #print(f"After p1_calc: {s}")
        s = str(p2_calc(s))

    return p1_calc(s)



def part2(v):
    num = 0
    for i in v:
        num += p2_calc(i)
    return num

print()
print(f"Part 1: {part1(var.copy())}")
print()
print(f"Part 2: {part2(var.copy())}")
print()