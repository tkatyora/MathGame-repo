import random
print('WELCOME TO MY MATH GAME')
start = input('press y to start and press q to exit: ').lower()
# the .lower() method is used so that upper letters are accepted
if start == 'y':
    print('INSERT THE ANSWERS OF THE QUESTIONS')
    x = random.randint(0 , 10)
    y = random.randint(0,20)
    sum = x + y
    answer = input(str(x)+' + '+ str(y)+': ')
    if answer == str(sum):
        print('wel done')
    else:
        print('try again later')

elif start == 'q':
    print('goodbye')
else:
   print('selected wrong option')

