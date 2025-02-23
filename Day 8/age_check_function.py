def age_check(age):
    if age>18:
        return True
    else:
        return False
    
try:
    age_input = int(input('Input your age: '))
    print(age_check(age_input))
except:
    print('Invalid input')
