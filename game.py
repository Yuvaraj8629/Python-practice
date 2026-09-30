import random
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
print("=" * 40)
print("     ROCK PAPER SCISSORS GAME")
print("=" * 40)
while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    choice = input("\nEnter your choice: ").strip()
    if choice == "4":
        print("\nThanks for playing!")
        print(f"Final Score - You: {player_score} | Computer: {computer_score}")
        break
    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Please choose 1, 2, or 3.")
        continue
    player_choice = choices[int(choice) - 1]
    computer_choice = random.choice(choices)
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print("🤝 It's a draw!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or
        (player_choice == "paper" and computer_choice == "rock")
        or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    print(f"Score → You: {player_score} | Computer: {computer_score}")
print("This project is now on GitHub!")