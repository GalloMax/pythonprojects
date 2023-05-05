number = int(input("Enter a number: "))
print([i for i in range(1, number + 1) if not(number % i)])
