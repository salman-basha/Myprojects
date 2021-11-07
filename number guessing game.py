import random

print("WELCOME TO THE NUMBER GUESSING GAME")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
number = random.randint(0, 9)
chances = 0
times = int(input("Enter how many chances you want: "))
print("GUESS THE NUMBER (between 0 to 9)")
print("Enter the number (between 0 to 9)")
while chances < times:
    guess = int(input("Enter number: "))
    if guess == number:
        print("CONGRATULATION YOU WON THE GAME.")
        break
    elif guess < number:
        print("your guess was too low: Guess a number higher than", guess)
        chances = chances+1
    else:
        print("your guess was too high: Guess a number lower than", guess)
        chances = chances+1
if not chances < times:
    print("YOU LOSE!!! THE NUMBER IS ", number)

