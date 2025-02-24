def counter():
    try:
        max_limit = int(input('Input a max limit: '))
        for i in range(max_limit + 1):
            print(i)  
            if i == max_limit:
                print('Counter finished')
                break
    except ValueError:
        print('Invalid input')

counter()