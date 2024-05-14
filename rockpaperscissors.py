import random

def get_user_choice():
    # Prompting the user to choose rock, paper, or scissors.
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    # Generating a random choice (rock, paper, or scissors) for the computer.
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    # Determining the winner based on the user's choice and the computer's choice
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, result):
    """Display the user's choice, computer's choice, and the game result."""
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("Congratulations! You win!")
    else:
        print("Sorry! Computer wins!")

def play_game():
    # Play a single round of Rock-Paper-Scissors
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)
    return result

def main():
    print("Welcome to Rock-Paper-Scissors!")

    user_score = 0
    computer_score = 0
    play_again = True

    while play_again:
        result = play_game()

        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'

    print("Thank you for playing Rock-Paper-Scissors")

if __name__ == "__main__":
    main()
