from random import Random
print('Mind Game')
print('select numbers from 1 to 100')
count = 1
fun = 1
number = Random().randint(1, 100)
while fun != 0:
    guess = int(input('Guess the number: '))
    if guess == number:
        print('congratulations, you won!')
        print('Well done you guessed correctly', count, 'attempt')
        break
    elif guess > 100:
        print('Invalid, Follow instruction (1 to 100) \n ******')
    elif guess < number:
        print('Wrong, your value is too low \n ******')
    elif guess > number:
        print('Wrong, your value is too high \n ******')
    count += 1
    if count > 5:
        fun = int(input('Show secret number Yes(0) or No(1):'))
        if fun > 1:
            print('i dare you')
            # break

else:
    print('Secret number is:', number)
    print('You made', count, 'attempt')
    print('Restart game')





