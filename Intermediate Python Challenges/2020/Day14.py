file = open("Day14Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]

def part1(v):
    mask = ""
    mem_num = False
    tot = {}
    for i in v:
        if i[0:2] == "ma":
            mask = i[7::]
        else:
            mem = i.split()[0]
            mem_num = bin(int(i.split()[2]))[2::]
            mem_num = ("0" * (36 - len(mem_num))) + mem_num
            for j in range(0, 36):
                if mask[j] != "X":
                    mem_num = mem_num[0:j] + mask[j] + mem_num[j + 1::]
            tot[mem] = int(mem_num, 2)
            
    num = 0
    for i in tot:
        num += tot[i]

    return num

def part2(v):
    mask = ""
    mem_num = False
    tot = {}
    for i in v:
        if i[0:2] == "ma":
            mask = i[7::]
        else:
            a = {}
            mem_num = int(i.split()[2])
            mem = bin(int(i.split("[")[1].split("]")[0]))[2::]
            mem = ("0" * (36 - len(mem))) + mem
            count = 0
            for j in range(0, 36):
                if mask[j] == "X":
                    a[count] = j
                    count += 1
                elif mask[j] == "1":
                    mem = mem[0:j] + "1" + mem[j + 1::]
            max_num = int(("1"*count), 2)
            for j in range(0, max_num + 1):
                temp_xs = bin(j)[2::]
                temp_xs = ("0" * (count - len(temp_xs))) + temp_xs
                temp_mem = mem[::]
                for k in range(0, count):
                    temp_mem = temp_mem[0:a[k]] + temp_xs[k] + temp_mem[a[k] + 1::]
                tot[int(temp_mem, 2)] = mem_num
                
    num = 0
    for i in tot:
        num += tot[i]

    return num

print(f"Part 1: {part1(var.copy())}")
print(f"Part 2: {part2(var.copy())}")