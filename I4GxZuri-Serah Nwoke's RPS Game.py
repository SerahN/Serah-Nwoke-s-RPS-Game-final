print("Hello, This is Serah's RPS Game")

is_running = True

while is_running:
    # Processing Game Output...
    user_operation = input("Are you ready to play? Pick any of['Y','N']")

    if user_operation == "Y":
        # initialize game module
        print("Serah's RPS Game Refreshed")

        # Ask user for input
        user_play = input(
            "What hand do you want to play? Pick any of[Rock,Paper,Scissors] ")

        if user_play == "Rock":
            print("User Play is Rock")

        elif user_play == "Paper":
            print("User Play is Paper")

        elif user_play == "Scissors":
            print("User Play is Scissors")

        else:
            # We get an invalid play when running it
            print("Invalid User Play")

    print("\nNow it's computer's turn...")
    while computer_play():
        computer_play = choice()
        choice = ['Rock', 'Paper', 'Scissors']
        print(computer_play)

# choice()
# print(choice)

if user_operation == "N":
    # stop RPS Game
    is_running = False
    print("Serah's RPS Game Stopped")
