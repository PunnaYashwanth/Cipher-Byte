import random

def generate_number(length):
    return ''.join(random.choices('0123456789', k=length))

def get_hint(secret, guess):
    hint = ['_'] * len(secret)
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            hint[i] = secret[i]
        elif guess[i] in secret:
            hint[i] = '?'
    return ' '.join(hint)

def play_round(secret, player_name):
    attempts = 0
    while True:
        guess = input(f"{player_name}, enter your guess (length {len(secret)}): ")
        attempts += 1
        if guess == secret:
            print(f"Correct! {player_name} guessed the number in {attempts} attempts.")
            return attempts
        else:
            hint = get_hint(secret, guess)
            print("Hint:", hint)

def mastermind_game():
    print("\n===============================")
    print("Welcome to Mastermind Game!")
    print("===============================\n")

    length = int(input("Enter the length of the number to guess: "))

    # Error handling for invalid input
    while length <= 0:
        print("Please enter a valid length greater than 0.")
        length = int(input("Enter the length of the number to guess: "))

    # Player 1 sets the number
    secret1 = input(f"Player 1, please set the number (length must be {length}): ")
    while len(secret1) != length or not secret1.isdigit():
        print(f"Please enter a valid number of length {length}.")
        secret1 = input(f"Player 1, please set the number (length must be {length}): ")

    # Player 2 guesses
    print("\nPlayer 2's turn to guess.")
    attempts2 = play_round(secret1, "Player 2")

    # Player 2 sets the number
    secret2 = input(f"Player 2, please set the number (length must be {length}): ")
    while len(secret2) != length or not secret2.isdigit():
        print(f"Please enter a valid number of length {length}.")
        secret2 = input(f"Player 2, please set the number (length must be {length}): ")

    # Player 1 guesses
    print("\nPlayer 1's turn to guess.")
    attempts1 = play_round(secret2, "Player 1")

    # Determine the winner
    if attempts1 < attempts2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts1 > attempts2:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    mastermind_game()

