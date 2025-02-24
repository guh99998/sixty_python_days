import random
import string 

def pass_generator():
    pass_size = int(input('Input the password size: '))
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''

    while len(password) < pass_size:
        password += random.choice(character)

    print(f'New password: {password}')

pass_generator()