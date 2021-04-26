import random

random_number = random.randint(1,10)
guess = None

while guess != random_number:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess > random_number:
        print("Number is lower")
    elif guess < random_number:
        print("Number is higher")
    else:
        print("You won!")
        print("Do you want to play again?")
        odp = input("y/n?: ")
        if odp == ("y"):
            print("Let's go!")
            random_number = random.randint(1,10)
            guess = None
        else:
            print("See ya next time")
            break