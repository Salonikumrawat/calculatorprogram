#Rock Paper Sccissors Game
import random

# Initialize scores
user_score = 0
computer_score = 0

# Available choices
choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    global user_score, computer_score
    print("\n--- Rock, Paper, Scissors ---")
    print("Type 'rock', 'paper', or 'scissors'")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"\nScores => You: {user_score} | Computer: {computer_score}")

def main():
    print("Welcome to Rock, Paper, Scissors Game!")
    while True:
        play_round()
        again = input("\nDo you want to play another round? (yes/no): ").lower()
        if again != 'yes':
            print("\nThanks for playing!")
            print(f"Final Score => You: {user_score} | Computer: {computer_score}")
            break

# Run the game
main()
