import random

options = ('stone', 'paper', 'scissors')
player_score = 0
computer_score = 0

print("Welcome to the Stone Paper Scissors game!\n")
print("You will play against the computer. The game will end when one of you reaches 5")

for i in range(5):
    computer = random.choice(options)
    player = input("Enter your choice (stone, paper, scissors): ").strip().lower()

    print(f"Your choice: {player}")
    print(f"Computer's choice: {computer}\n")

    if player == computer:
        print(f"Both players selected {player}. It's a tie.\n")

    elif player == "stone":
        if computer == "paper":
            print("Paper covers stone. I win!\n")
            computer_score += 1
        else:
            print("Stone crushes scissors. You win!\n")
            player_score += 1

    elif player == "paper":
        if computer == "scissors":
            print("Scissors cuts paper. I win!\n")
            computer_score += 1
        else:
            print("Paper covers stone. You win!\n")
            player_score += 1

    elif player == "scissors":
        if computer == "stone":
            print("Stone crushes scissors. I win!\n")
            computer_score += 1
        else:
            print("Scissors cuts paper. You win!\n")
            player_score += 1

    else:
        print("Input didn't match. Please try again.\n")

print("Time for the final result. Let's see who wins the game!!\n")
print(f"Your final score: {player_score}")
print(f"Computer's final score: {computer_score}\n")

if player_score > computer_score:
    print("You win the game!! 🎉")
elif player_score == computer_score:
    print("It's a tie game!! 🤝")
else:
    print("Computer wins the game!! 🤖")