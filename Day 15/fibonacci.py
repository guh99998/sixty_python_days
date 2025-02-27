fibonacci = [0, 1]

for i in range(8):
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_number)

print(fibonacci)