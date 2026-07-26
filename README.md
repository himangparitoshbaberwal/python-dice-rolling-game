# 🎲 Dice Rolling Game

A simple **multiplayer dice rolling game built with Python**.
Players take turns rolling a six-sided die and try to reach the selected winning score first.

The game also includes input validation, score tracking, and a risk/reward mechanic where rolling a **1 causes the player to lose all their points**.

---

## 🎮 Features

* 👥 Supports **2–4 players**
* 🎯 Players can choose the **winning score**
* 🎲 Random six-sided dice rolls
* 💥 Rolling a **1 resets the player's score to 0**
* 🛑 Players can choose to stop their turn
* 📊 Live scoreboard after every turn
* ✅ Input validation for:

  * Number of players
  * Winning score
  * Roll/stop choices
* 🏆 Automatically detects the winner

---

## 🕹️ How to Play

1. Start the program.
2. Enter the number of players (**2–4**).
3. Choose the maximum score required to win.
4. Players take turns.
5. On your turn:

   * Enter `y` to roll the dice.
   * Enter `n` to end your turn.
6. Every roll adds the dice value to your score.
7. **If you roll a 1, your entire score becomes 0.**
8. The first player to reach or exceed the maximum score wins.

### Example

```text
🎮 Player 1's Turn
Current Score: 15

Roll the dice? (y/n): y
🎲 You rolled: 5
✅ Your total score is now 20

Roll the dice? (y/n): n
You ended your turn with 20 points.
```

If the player rolls a `1`:

```text
🎲 You rolled: 1
💥 Oops! You rolled a 1.
💥 You lose ALL your points!
```

---

## 🧠 Game Rules

| Event               | Result                            |
| ------------------- | --------------------------------- |
| Roll `2–6`          | Dice value is added to your score |
| Roll `1`            | Your score becomes `0`            |
| Enter `n`           | End your current turn             |
| Reach winning score | You win the game                  |

---

## 🛠️ Technologies Used

* **Python 3**
* Python `random` module
* `while` loops
* `for` loops
* Functions
* Lists
* Exception handling (`try` / `except`)
* Conditional statements
* User input handling

---

## 📂 Project Structure

```text
Dice-Rolling-Game/
│
├── dice_game.py
└── README.md
```

---

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone YOUR_REPOSITORY_LINK
```

### 3. Navigate to the project folder

```bash
cd Dice-Rolling-Game
```

### 4. Run the game

```bash
python dice_game.py
```

---

## 💡 Concepts Practiced

This project helped practice several important Python concepts:

* **Functions** for organizing reusable code
* **Loops** for managing game flow
* **Lists** for storing player scores
* **Random numbers** for dice simulation
* **Input validation** for handling incorrect user input
* **Exception handling** using `try` and `except`
* **Game state management**
* **Formatted output** using f-strings

---

## 🚀 Possible Improvements

Some ideas for future versions:

* 🤖 Add a **computer/AI opponent**
* 🎨 Add a graphical interface using **Tkinter** or **Pygame**
* 💾 Save high scores to a file
* 🏅 Add a leaderboard
* 🔄 Add a replay option
* 🎲 Add different types of dice
* ⚙️ Add difficulty levels
* 👤 Allow players to enter custom names
* 📈 Track statistics such as total rolls and highest score

---

## 👨‍💻 Author

**Himang Paritosh Baberwal**

Built as a beginner Python project to practice programming fundamentals and game logic.

---