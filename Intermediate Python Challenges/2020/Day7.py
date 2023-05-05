file = open("Day7Input.txt", "r")
var = file.readlines()
file.close()
for i in range(0, len(var)):
    var[i] = var[i].split("\n")[0]

d = {}
dr = {}
n = {}


for i in range(0, len(var)):
    temp = var[i].split("contain")
    bag = temp[0].split()[0] + " " + temp[0].split()[1]
    temp = temp[1].split(",")
    d[bag] = []
    n[bag] = {}
    t = {}
    for j in temp:
        if (j.split()[1] + " " + j.split()[2]) != "other bags.":
            
            d[bag].append(j.split()[1] + " " + j.split()[2])
            t[(j.split()[1] + " " + j.split()[2])] = int(j.split()[0])
    n[bag] = t
    var[i] = bag

print(d)


for i in var:
    dr[i] = []
    for j in var:
        if i in d[j]:
            dr[i].append(j)
print(dr)

def get_bags(current):
    num = 0
    if len(d[current]):
        d[current] = []
        num = 1
        for i in dr[current]:
            num = num + get_bags(i)
    return num

def get_inside_bags(current):
    num = 1
    for i in d[current]:
        num = num + n[current][i]*get_inside_bags(i)
    return num

print(get_inside_bags("shiny gold") - 1)
