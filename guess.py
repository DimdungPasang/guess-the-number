import random

def guess(x):
    random_num = random.randint(1,x)

    guess = 0
    while random_num != guess:
        guess = int(input(f"Guess a number bewteen 1 and {x}: "))
        if(guess > random_num):
            print("Sorry, your guess is too high")
        elif (guess < random_num):
            print("Sorry, your guess is too low")
    print(f"Yay! Your guess {random_num} is correct")

guess(10)