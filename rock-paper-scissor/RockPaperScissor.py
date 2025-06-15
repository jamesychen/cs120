from random import randint

# List of valid plays (all lowercase)
t = ["rock", "paper", "scissors"]

# Assign random play to computer
computer = t[randint(0, 2)]

# Start game loop
player = False

while not player:
    player = input("Rock, Paper, Scissors? ").lower()
    
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    
    player = False
    computer = t[randint(0, 2)]