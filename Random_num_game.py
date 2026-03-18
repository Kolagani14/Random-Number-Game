import random

while True:
    print("\n--- Number Duel Game ---")

    human = int(input("Enter your number (1-100): "))

    if human < 1 or human > 100:
        print("Enter number between 1 and 100 only.")
        continue

    computer = random.randint(1, 100)

    print(f"Computer chose: {computer}")

    if human == computer:
        print("It's a TIE!")
    elif human > computer:
        print("You WIN!")
    else:
        print("Computer WINS!")

    choice = input("Play again? (y/n): ")
    if choice.lower() != 'y':
        print("Game Over.")
        break