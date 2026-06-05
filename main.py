# To clear the terminal
print("\033c", end="")

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

while True:
        # Ask if the user's want a re match or at the beginning to just start the game
        rematch = input("You want to get a re-match? type (y/n) ").lower()
        print("")

        if rematch == "y" and "Y":

            # The Game Code Start

            # Checks if either player one or player two win's
            if Player_one > Player_two:
                print("")
                print("Player one wins")

            elif Player_two > Player_one:
                print("Player two wins")

            else:
                print("It's a tie")

            print("The numbers you both got was ...")
            print()

            # Prints out player ones and player two's nmuber's
            print("Player 1 rolls a", Player_one)

            print("Player 2 rolls a", Player_two)
            print("")

            # So it re rolls the numbers so it doesn't stay the same number the whole time or keep the same numbers and makes one player always win
            if Player_one != 11:
                    Player_one = random.randint(1, 10)

            if Player_two != 11:
                    Player_two = random.randint(1, 10)

            # The Game Code End

            
        if rematch == "n":
            print("Bye but thanks for playing my RNG game")

            # Breaks the user out of the loop
            break

        # The Anti Cheat so they can't just spam enter to keep getting re matches
        if rematch ==  "":
            print("")
            print("Nice try play the game the right way ")
            print("")
            break