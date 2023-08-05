lines = []
with open("1.input") as f:
    lines = f.readlines()
    lines = [i.rstrip("\n") for i in lines]

calories = []
curr_calories = 0
for i, j in enumerate(lines):
    if j == '' or i == len(lines) - 1:
        calories.append(curr_calories)
        curr_calories = 0
    else: curr_calories += int(j)

print(sum(sorted(calories)[len(calories)-3::]))