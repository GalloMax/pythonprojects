def print_top(x):
    print(" ---" * x)

def print_side(x):
    print("|   " * x)


side_length = int(input("Enter grid side length: "))
if side_length <= 0:
    quit("Please enter something above 0")

for i in range(0,side_length):
    print_top(side_length)
    print_side(side_length + 1)

print_top(side_length)