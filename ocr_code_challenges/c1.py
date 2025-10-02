import random

def count_correct_digits(secret, guess):
    # Count how many digits in guess are also in secret (regardless of position)
    secret_list = list(secret)
    guess_list = list(guess)
    count = 0
    for digit in guess_list:
        if digit in secret_list:
            count += 1
            secret_list.remove(digit)  # Prevent double-counting
    return count

def main():
    secret_number = str(random.randint(1000, 9999))
    tries = 0

    print("Guess the 4-digit number!")

    while True:
        guess = input("Enter your 4-digit guess: ").strip()
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        tries += 1
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {tries} tries.")
            break
        correct = count_correct_digits(secret_number, guess)
        print(f"You got {correct} digit(s) correct.")

if __name__ == "__main__":
    main()