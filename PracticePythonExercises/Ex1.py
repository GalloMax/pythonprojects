name = input("What is your name?")
age = int(input("What is your age?"))

if age > 100 or age < 0:
    print("error")
    quit()
else:
    year = 2021 + (100 - age)
    print("Hi " + name + ", if this year is 2021, then you will turn 100 in the year " + str(year))
