import random

# Get user input
name = input("Enter your name: ")
your_team_name = input("Enter your team name: ")
opposition_team = input("Enter the opponent team name: ")

# Toss the coin
toss_result = random.choice(["heads", "tails"])

# Check if user won the toss
if input("Heads or tails? ").lower() == toss_result:
    print("Congratulations! You won the toss.")
    choice = input("What will you choose, bat or bowl? ").lower()
    if choice == "bat":
        print(f"{name}, you chose to bat for {your_team_name}.")
    elif choice == "bowl":
        print(f"{name}, you chose to bowl for {your_team_name}.")
    else:
        print("Invalid choice. Please choose 'bat' or 'bowl'.")
else:
    print(f"{name}, you lost the toss.")
    computer_choice = random.choice(["bat", "bowl"])
    print(f"The opponent team, {opposition_team}, chose to {computer_choice}.")
