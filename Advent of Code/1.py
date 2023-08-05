lines = []

with open("1.input") as f:
    lines = f.readlines()
    lines = [i.rstrip("\n") for i in lines]

count = 0
curr_total = 0
max_count = 0
max = 0
for i in lines:
    if i == '':
        count += 1
        curr_total = 0
    else:
        curr_total += int(i)
        if curr_total > max:
            max_count = count
            max = curr_total

print(max, max_count)