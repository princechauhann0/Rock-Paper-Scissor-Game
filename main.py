# ROCK PAPER ScISSOR GAME

import random

def determine_winner(player, computer):
    """Determine the result of a single round."""
    if player == computer:
        return "It's a tie!"
    elif (player == 'r' and computer == 's') or \
         (player == 'p' and computer == 'r') or \
         (player == 's' and computer == 'p'):
        return "You Win!"
    else:
        return "You Lose!"

# Mapping shorthand input to full names
options = {"r": "Rock", "p": "Paper", "s": "Scissor"}

print("Welcome to Rock Paper Scissor")
print("Enter your choice:")
print(" r - Rock")
print(" p - Paper")
print(" s - Scissor\n")

# Take number of rounds
while True:
    try:
        rounds = int(input("How many rounds do you want to play? "))
        if rounds <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

user_score = 0
computer_score = 0

# Play multiple rounds
for i in range(rounds):
    print(f"\nRound {i + 1}")
    user_input = input("Your choice (r/p/s): ").lower()

    if user_input not in options:
        print("Invalid choice! You lost this round.")
        computer_score += 1
        continue

    computer = random.choice(['r', 'p', 's'])
    print(f"Computer chose: {options[computer]}")

    result = determine_winner(user_input, computer)
    print(result)

    if "Win" in result:
        user_score += 1
    elif "Lose" in result:
        computer_score += 1

# Final Results
print("\nFINAL SCORE")
print(f"Your Score: {user_score}")
print(f"Computer Score: {computer_score}")

if user_score > computer_score:
    print("Congratulations! You won the match.")
elif user_score < computer_score:
    print("You lost. Better luck next time.")
else:
    print("It's an overall tie!")
