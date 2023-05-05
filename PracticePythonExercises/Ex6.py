string = input("Enter a string: ")

for i in range(len(string)):
    if string[i] != string[len(string) - 1 - i]:
        print("Not a palindrome")
        quit()
print("It is a palindrome")
