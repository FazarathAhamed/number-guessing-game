import random

def get_difficulty():
    """Let the player choose difficulty level."""
    print("\n🎮 Choose Difficulty:")
    print("  1. Easy   (1–50,  10 chances)")
    print("  2. Medium (1–100,  7 chances)")
    print("  3. Hard   (1–200,  5 chances)")

    while True:
        choice = input("\nEnter 1, 2, or 3: ").strip()
        if choice == "1":
            return 50, 10, "Easy"
        elif choice == "2":
            return 100, 7, "Medium"
        elif choice == "3":
            return 200, 5, "Hard"
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


def play_game():
    """Main game logic."""
    print("=" * 40)
    print("   🔢 NUMBER GUESSING GAME")
    print("=" * 40)

    max_number, max_attempts, level = get_difficulty()
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\n✅ [{level}] I picked a number between 1 and {max_number}.")
    print(f"   You have {max_attempts} chances. Good luck!\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} | Guess: "))
        except ValueError:
            print("⚠️  Please enter a valid number!\n")
            continue

        attempts += 1

        if guess < 1 or guess > max_number:
            print(f"⚠️  Out of range! Enter a number between 1 and {max_number}.\n")
            attempts -= 1  # Don't count invalid range guess
            continue

        if guess == secret_number:
            print(f"\n🎉 CORRECT! The number was {secret_number}!")
            print(f"   You got it in {attempts} attempt(s)! 🏆")
            return True
        elif guess < secret_number:
            print(f"   📈 Too LOW!  ({remaining - 1} chances left)\n")
        else:
            print(f"   📉 Too HIGH! ({remaining - 1} chances left)\n")

    print(f"\n💀 GAME OVER! The number was {secret_number}. Better luck next time!")
    return False


def main():
    """Entry point — handles replay."""
    while True:
        play_game()
        again = input("\n🔄 Play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n👋 Thanks for playing! Goodbye!\n")
            break


if __name__ == "__main__":
    main()
