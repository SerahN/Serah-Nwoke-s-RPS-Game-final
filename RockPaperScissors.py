# import random module
import random

# User welcome message
print("Hello, This is Serah's Game of Rock Paper Scissors")

# Instruct user on the rules of the game
print("Here are the rules to win this Rock Paper Scissors Game: \n"
      + "Rock vs Scissors->Rock wins \n"
      + "Rock vs Paper->Paper wins \n"
      + "Paper vs Scissors->Scissors wins \n")

is_running = True

while is_running:
    user_operation = input(
        "Are you ready to play? Pick any of['Y', 'y', 'N', 'n']")

    if user_operation == "Y" or user_operation == 'y':
        # start game
        print("Serah's Game of RPS Refreshed")

        # Accept user play
        print("Make your play: \n 1 for Rock, \n 2 for Paper, and \n 3 for Scissors \n")
        play = int(input("User play: "))

        while play > 3 or play < 1:
            play = int(input("enter valid input: "))

        if play == 1:
            play_name = 'Rock'
        elif play == 2:
            play_name = 'Paper'
        else:
            play_name = 'Scissors'

        print("User play is: " + play_name)
        print("\nNow its computer turn to play, please wait...")

        # Computer chooses a random number/ game play
        comp_play = random.randint(1, 3)

        while comp_play == play:
            comp_play = random.randint(1, 3)

        if comp_play == 1:
            comp_play_name = 'Rock'
        elif comp_play == 2:
            comp_play_name = 'Paper'
        else:
            comp_play_name = 'Scissors'

        print("Computer play is: " + comp_play_name)

        print(play_name + " V/s " + comp_play_name)

        # Who is the WINNER?
        if play == comp_play:
<<<<<<< HEAD
            print(f"User and Computer selected {play_name}. It's a tie!")
        elif((play == 1 and comp_play == 2) or
=======
            print("\nUser and Computer played {play_name}. It's a tie!")
        if((play == 1 and comp_play == 2) or
>>>>>>> 7d2c670f8ff69bfc8d69c936e62f221ada61e024
                (play == 2 and comp_play == 1)):
            print("Paper wins => ", end="")
            result = "Paper"

        elif((play == 1 and comp_play == 3) or
             (play == 3 and comp_play == 1)):
            print("Rock wins =>", end="")
            result = "Rock"
        else:
            print("Scissors wins =>", end="")
            result = "Scissors"

        if result == play_name:
            print("<== User is the WINNER! ==>")
        else:
            print("<== Computer is the WINNER! ==>")
            continue

    if user_operation == 'N' or user_operation == 'n':
        # stop loop and end game
        is_running = False
        print("\nSerah's Game of RPS Over!")
