import random

random_number = random.randint(1, 100)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Guess a number between 1-100:  ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please Type A Number')
        continue
    if user_guess == random_number:
        print('You Got The Number')
        break
    elif user_guess > random_number:
        print('You Were Above The Number')
    else:
        print('You Were Below The Number')
    
print('You got it in', guesses, 'guesses')
    