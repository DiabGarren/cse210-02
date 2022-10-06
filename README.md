# Hilo

Hilo is a quick game where the player is guessing what will be the next card drawn by the dealer, higher or lower than the current one. If the player guesses correctly, more points are earned! But that doesn't happen if the guess is wrong... Are you lucky enough to win?

## Game Specifics:

---

# Objects & Responsibilities/Behavior

• Inform user they have 300 points & point system, guess right +100, guess wrong -75, when 0 game ends
• Begin with showing random card -> no user guess yet
• Then user guess will next card be higher or lower -> user input Higher or Lower  
• If statements & Conditionals -> while user points != 0, keep playing
• Stored point calculator
• Display current total after each guess
• When player has 0 points program stops  
• Kill program at end if player chooses no

# Object Design -> Class Design

• object user -> class user
• object total -> class total
• random_card

## object: User

    # Resposibility:
    - to guess if the next card displayed would be higher or lower than the current card displayed.

    # Behaviours:
    - pick between higher or lower
    - decide to play again or not

    # State:
    - Higher or Lower
    - Play again?

## object: Total

    # Responsibility:
    - to sum up all user's player score and display the total

    # Behaviours:
    - display total score

    # State:
    - user score

## Project Structure

---

The project files and folders will be organized as follows:

```
root                    (project root folder)
+-- hilo                (source code for game)
  +-- game              (specific classes)
  +-- main.py       (program entry point)
+-- README.md           (general info)
```

# Other

• import random Ex: -> random_card = random.randit(1, 13) \*Can assign alias to random but not necessary. Ex: import random as r -> r.randit(1,13)
• import .py from user to main file

## Rules

---

• The player starts the game with 300 points.
• Individual cards are represented as a number from 1 to 13.
• The current card is displayed.
• The player guesses if the next one will be higher or lower.
• The next card is displayed.
• The player earns 100 points if they guessed correctly.
• The player loses 75 points if they guessed incorrectly.
• If a player reaches 0 points the game is over.
• If a player has more than 0 points, they decide if they want to keep playing.
• If a player decides not to play again the game is over.

## Required Technologies

---

- Python 3.8.0

## Authors: TEAM E

---

- Mazzarella-Woelzl, Alison Reed
- Saenz, Paula
- Shevtsov, Denis
- Ogboanoh, Richard Oshiomole Ephraim
- Diab, Garren Mark
