def start_game():
    print("\nWelcome, Recruiter!")
    print("You have 3 amazing candidates in front of you.")
    print("Only ONE is actually worth hiring.\n")

    print("A - Talks well, but no real projects.")
    print("B - Knows theory, but never shipped anything.")
    print("C - Builds, ships, improves constantly.\n")

    choice = input("Who do you hire? (A/B/C): ").strip().upper()

    if choice == "A":
        print("\nYou chose A.")
        print("Good communication, but lacks execution.")
        print("Result: Missed opportunity.\n")
    elif choice == "B":
        print("\nYou chose B.")
        print("Strong fundamentals, but no real-world output.")
        print("Result: Not ready yet.\n")
    elif choice == "C":
        print("\nYou chose C.")
        print("Delivers real projects, focuses on results.")
        print("Result: You found your developer.\n")
    else:
        print("\nInvalid choice. Recruiters need attention to detail.\n")

    replay = input("Try again? (yes/no): ").strip().lower()
    if replay == "yes":
        start_game()
    else:
        print("\nThanks for playing.")

if __name__ == "__main__":
    start_game() 