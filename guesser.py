# importing random from randint
from random import randint
try_count = 0
max_tries = 5

print('Hello! What is your name')
myName = input()
answer = randint(1, 20)
print('Anyway, ' + myName + ', I am thinking of a number between 1 and 20.')

#print(str(answer) + " is ans")

while try_count < max_tries:
    try:
        guess = int(input('Can you guess?  '))

        if 0 < guess > 20:
            print('hello buddy, i said, from 1-20')
            continue

        try_count += 1
            
        if guess != answer and try_count == max_tries:
            print('Nope. The number I was thinking of was ' + str(answer))
            break
        if int(guess) < answer:
            print('number is too low')
        if int(guess) > answer:
            print('number is too high')  
        if int(guess) == answer:
            print('Good job, ' + myName + '! You guessed my number in ' + str(try_count) + ' guesses!')
            break    
    except ValueError:
        print('please enter a number')
