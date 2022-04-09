import random

#user
def guess(x):
    random_num = random.randint(1,x)

    guess = 0
    while random_num != guess:
        guess = int(input(f"Guess a number bewteen 1 and {x}: "))
        if (guess > random_num):
            print("Sorry, your guess is too high")
        elif (guess < random_num):
            print("Sorry, your guess is too low")
    print(f"Yay! Your guess {random_num} is correct")

# guess(10)

#computer
def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    #it loops until the user's feedback isn't correct ie. c
    while(feedback != 'c'):
        if(low != high):
            guess = random.randint(low,high) #computer randomly guesses a number bewteen low and high
        else:
            guess = low

        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C): ').lower() #asks for user's feedback until its correct

        if (feedback == 'h'):
            print(f"Your guess {guess} is too high")
            high = guess - 1  #if guess is too high then to make sure computer doesn't guess number greater than that
        elif (feedback == 'l'):
            print(f'Your {guess} is too low') 
            low = guess + 1  #if guess is too low then to make sure computer doesn't guess number less than that
            
    print(f'Yay! Computer guessed your number {guess} correctly.')

computer_guess(1000)