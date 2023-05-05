num = int(input("how many Fibonacci numbers to generate: "))
if not num: quit("entered 0")
x = 1
y = 0
temp = 0
for i in range(0, num):
    print(x)
    temp = x
    x = x + y
    y = temp

