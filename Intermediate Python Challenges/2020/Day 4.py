file1 = open("Day4Input.txt", "r")
passports = []
line = file1.readline()
passport = []
valid_num = 0
passport_num = 0
d = {"byr": 0, "iyr": 1, "eyr": 2, "hgt": 3, "hcl": 4, "ecl": 5, "pid": 6, "cid": 7}


def good_passport(v):
    for m in range(0, 7):
        if v[m] == 0:
            return False
    return True


while line:
    if line.split("\n")[0]:
        if len(passports) == passport_num:
            passports.append(line.split("\n")[0])
        else:
            passports[passport_num] = passports[passport_num] + ' ' + line.split("\n")[0]
    else:
        passport_num = passport_num + 1
    line = file1.readline()

for i in range(0, len(passports)):
    passport = passports[i].split()
    valid = [0, 0, 0, 0, 0, 0, 0, 0]
    fields = [0, 0, 0, 0, 0, 0, 0, 0]
    if len(passport) >= 7:
        for j in range(0, len(passport)):
            valid[d[passport[j].split(":")[0]]] = 1
            fields[d[passport[j].split(":")[0]]] = passport[j].split(":")[1]
        if good_passport(valid):
            fields[0] = int(fields[0])
            fields[1] = int(fields[1])
            fields[2] = int(fields[2])
            height_type = fields[3][(len(fields[3]) - 2): len(fields[3])]
            if height_type != "cm" and height_type != "in":
                fields[3] = -1
            else:
                fields[3] = int(fields[3][0:(len(fields[3]) - 2)])
            hair_color = 0
            hair_options = "0123456789abcdef"
            if len(fields[4]) == 7:
                if fields[4][0] == "#":
                    hair_color = 1
                    for k in range(1, 7):
                        if fields[4][k] not in hair_options:
                            hair_color = 0
            eye_color = 0
            eye_options = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if fields[5] in eye_options:
                eye_color = 1

            if 1920 <= fields[0] <= 2002:
                if 2010 <= fields[1] <= 2020:
                    if 2020 <= fields[2] <= 2030:
                        if (height_type == "cm" and 150 <= fields[3] <= 193) or (height_type == "in" and 59 <= fields[3] <= 76):
                            if hair_color:
                                if eye_color:
                                    if len(fields[6]) == 9:
                                        valid_num = valid_num + 1

print(valid_num)
file1.close()
