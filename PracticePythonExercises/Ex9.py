import random

a = random.randint(1,9)
tries = 0

while True:
    num = input("Guess a number [1,9]: ")
    if num == "exit":
        print("Tries: " + str(tries))
        break

    tries = tries + 1
    num = int(num)

    if num == a:
        print("exactly right!")
        print("Tries: " + str(tries))
        break
    elif num < a:
        print("too low")
    else:
        print("too high")


