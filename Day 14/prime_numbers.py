number = int(input("Input a number to check: "))
is_prime = True

if number <= 1:
    is_prime = False

for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print(f'{number} is prime')
else:
    print(f'{number} is not prime')