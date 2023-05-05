def get_divisors(num) -> list:
    return [i for i in range(1, num + 1) if not (num % i)]


number = int(input("Enter a number: "))
if len(get_divisors(number)) < 3 and number > 0:
    print("It is a prime number")
else:
    print("It is not a prime number")
