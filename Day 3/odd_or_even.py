try:
    number = int(input("Input a number: "))
    if number % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")
except ValueError:
    print("The input isn't a int number")