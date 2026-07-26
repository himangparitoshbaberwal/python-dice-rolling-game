import random

# -------------------- Functions -------------------- #

def roll():
    """Roll a six-sided die."""
    return random.randint(1, 6)


def get_number_of_players():
    """Get a valid number of players."""
    while True:
        try:
            players = int(input("Enter the number of players (2-4): "))
            if 2 <= players <= 4:
                return players
            else:
                print("❌ Please enter a number between 2 and 4.")
        except ValueError:
            print("❌ Invalid input! Please enter an integer.")


def get_max_score():
    """Get the winning score."""
    while True:
        try:
            max_score = int(input("Choose the maximum score to win: "))
            if max_score > 0:
                return max_score
            else:
                print("❌ Score must be greater than 0.")
        except ValueError:
            print("❌ Invalid input! Please enter an integer.")


def display_scores(scores):
    """Display all players' scores."""
    print("\n========== SCOREBOARD ==========")
    for i, score in enumerate(scores, start=1):
        print(f"Player {i}: {score}")
    print("=" * 32)


# -------------------- Main Program -------------------- #

print("=" * 40)
print("🎲 Welcome to the Dice Rolling Game 🎲")
print("=" * 40)

players = get_number_of_players()
max_score = get_max_score()

player_scores = [0] * players

winner = None

while winner is None:

    for player in range(players):

        print(f"\n🎮 Player {player + 1}'s Turn")
        print(f"Current Score: {player_scores[player]}")

        turn_score = player_scores[player]

        while True:

            choice = input("Roll the dice? (y/n): ").strip().lower()

            if choice == "y":

                dice = roll()
                print(f"🎲 You rolled: {dice}")

                if dice == 1:
                    print("💥 Oops! You rolled a 1.")
                    print("💥 You lose ALL your points!")
                    turn_score = 0
                    player_scores[player] = turn_score
                    break

                turn_score += dice
                player_scores[player] = turn_score

                print(f"✅ Your total score is now {turn_score}")

                if turn_score >= max_score:
                    winner = player
                    break

            elif choice == "n":
                print(f"You ended your turn with {turn_score} points.")
                player_scores[player] = turn_score
                break

            else:
                print("❌ Please enter only 'y' or 'n'.")

        display_scores(player_scores)

        if winner is not None:
            break

# -------------------- Game Over -------------------- #

print("\n" + "=" * 40)
print("🏆 GAME OVER 🏆")
print("=" * 40)

display_scores(player_scores)

print(f"\n🎉 Congratulations! Player {winner + 1} wins the game! 🎉")