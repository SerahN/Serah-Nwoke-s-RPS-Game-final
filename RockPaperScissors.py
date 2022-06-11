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
        print("Make your play: \n 'R' for Rock, \n 'P' for Paper, and \n 'S' for Scissors \n")
        playlist = ['R', 'P', 'S']
        play = str(input("User play: "))

        if play == 'R':
            play_name = 'Rock'
        elif play == 'P':
            play_name = 'Paper'
        elif play == 'S':
            play_name = 'Scissors'
        else:
            print("Invalid User Play")
            continue

        print("User play is: " + play_name)
        print("\nNow its computer turn to play, please wait...")

        # Computer chooses a random game play
        comp_play = random.choice(playlist)

        while comp_play == play: 
            comp_play = random.choice(playlist)

        if comp_play == 'R':
            comp_play_name = 'Rock'
        elif comp_play == 'P':
            comp_play_name = 'Paper'
        elif comp_play == 'S':
            comp_play_name = 'Scissors'

        print("Computer play is: " + comp_play_name)

        print(play_name + " V/s " + comp_play_name)

        # Who is the WINNER?
        if play == comp_play:
            print(f"User and Computer selected {play_name}. It's a tie!")
        elif((play == 'R' and comp_play == 'P') or
                (play == 'P' and comp_play == 'R')):
            print("Paper wins => ", end="")
            result = "Paper"

        elif((play == 'R' and comp_play == 'S') or
             (play == 'S' and comp_play == 'R')):
            print("Rock wins =>", end="")
            result = "Rock"
        elif((play == 'P' and comp_play == 'S') or
             (play == 'S' and comp_play == 'P')):
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