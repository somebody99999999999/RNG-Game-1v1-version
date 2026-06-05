# The name of the program
# RNG Game

# The import of the random module
import random

# Intro and Instructions to the program / game
print("Hello and welcome to RNG Game press Enter / Return")
input()
print("🔴 INSTRUCTIONS 🔴")
print(" Whoever gets the higher number wins! ")
print("Press Enter / Return to start the game ")
input()

# Generate the first random pair numbers from between one and any number
Player_one = random.randint(1, 10)

# Generate the second random pair numbers between one and any number
Player_two = random.randint(1, 10)

reset_game = True

while True:
    # Checks either if player one or 2 won
    if Player_one > Player_two:
        print("Player 1 Wins!")

    elif Player_two > Player_one:
        print("Player 2 Wins!")

    else:
        print("It's a Tie!")

    print("The numbers you both got was ...")
    input()

    # Prints out player ones and player two's nmuber's
    print("Player 1 rolls a", Player_one)

    print("Player 2 rolls a", Player_two)

    # So it doesn't reroll if there is a ten aleady on the board
    Player_one = random.randint(1, 10)

    Player_two = random.randint(1, 10)

    # Ask the user for a re-roll
    reroll = input("You want to get a reroll? (y/n) ").lower()

    if reroll == "n":
        print("Bye but thanks for playing my RNG game")
       
        # Breaks out of the loop
        break