# The name of the program
# RNG Game 1v1 version

# The import of the random module
import random

# Intro and Instructions to the program / game
print("Hello and welcome to RNG Game press Enter / Return")
input()
print("🔴 INSTRUCTIONS 🔴")
print(" Whoever gets the higher number wins ")
print("Press Enter / Return to start the game ")
input()

# Generates player ones number from one and any number
Player_one = random.randint(1, 10)

# Generates player two's number from one and any number
Player_two = random.randint(1, 10)

reset_game = True

while True:
    # Checks if either player one or player two win's
    if Player_one > Player_two:
        print("Player one wins")

    elif Player_two > Player_one:
        print("Player two wins")

    else:
        print("It's a tie")

    print("The numbers you both got was ...")
    input()

    # Prints out player ones and player two's nmuber's
    print("Player 1 rolls a", Player_one)

    print("Player 2 rolls a", Player_two)

    # Ask if the user's want a re match
    rematch = input("You want to get a re-match? ").lower()

    if rematch == "n":
        print("Bye but thanks for playing my RNG game")

        # Breaks out of the loop
        break

    if rematch == "y" and "Y":
        print("ok")