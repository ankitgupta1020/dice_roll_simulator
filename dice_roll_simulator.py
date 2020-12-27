import random
while True:
    print('''1. 1roll the dice          2. exit    ''')
    user = int(input("What you wanna do\n"))
    if user==1:
        number = random.randint(1,6)
        print(number)
    else:
        break