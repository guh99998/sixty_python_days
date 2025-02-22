fruit_list = ["Apple", "Banana", "Watermelon", "Blueberry", "Orange", "Coconut", "Blackberry", "Cherry", "Lemon"]

new_fruit = input("Input any fruit: ")

fruit_list.append(new_fruit)

for fruit in fruit_list:
    print(fruit)



new_fruit_list = []

while True:
    fruit = input("Input some fruit or 'exit': ")
    if fruit == "exit":
        break
    new_fruit_list.append(fruit)

print(new_fruit_list)