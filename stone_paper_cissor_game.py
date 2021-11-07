import random

game_list = ['Rock', 'Paper', 'Scissor']
computer = c = 0
command = p = 0
print("Score: Computer" + str(c) + "player" + str(p))

# running the loop
run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("Enter the value 'Rock', 'Paper', 'Scissor' or 'Quit':").capitalize()
    if command == computer_choice:
        print("Tie")
    elif command == "Rock".capitalize():
        if computer_choice == 'scissor'.capitalize():
            print("Player Won!")
            p += 1
        else:
            print("Computer Won!")
            c += 1
    elif command == "paper".capitalize():
        if command == 'rock'.capitalize():
            print("Player Won!")
            p += 1
        else:
            print("Computer Won!")
            c += 1
    elif command == "scissor".capitalize():
        if computer_choice == 'paper'.capitalize():
            print("Player Won!")
            p += 1
        else:
            print("Computer Won!")
            c += 1
    elif command == 'quit'.capitalize():
        break
    else:
        print("Wrong command! ")

    print("player: " + command)
    print("computer: " + computer_choice)
    print("")
    print("Score: Computer " + str(c) + "Player " + str(p))
    print("")
