# Import the user and card classes from their respective modules
from card import Card
from user import User


def main():
    print(
"To play the game is very simple, you will start with 300 points. \
To begin you will be shown a card at random. You will need to guess \
whether you think the next card will be higher in value or lower. \
Guess right and you earn 100 points. Guess wrong and you will lose \
75. Reach 1,000 points and you win the game, reach 0 and you lose.\
\nGood luck!\n")

    # Initialize a card object
    card = Card()
    # Give the card a random value
    card.next_card()

    # Initialize a user object
    # Creates a user object with a score of 300 point
    user = User()

    # Loop as long as the user has points
    while user.score > 0:
        # Display the card value and the user score
        print(f"The card is: {card.prev_value}")
        print(f"Your score is {user.score}")
        # Get the guess from the user
        guess = str(input(
            "Please enter whether you think the next card will be higher or lower. (h/l)\n").lower())
        # Display the next card value
        print(f"Next card was: {card.value}")

        # Let player only use l or h, and not other letter
        while guess != "l" and guess != "h":
            print("You need to choose between only h or l!")
            guess = str(input(
                "Please enter whether you think the next card will be higher or lower. (h/l)\n").lower())

        # Set if the guess was correct or not
        correct_guess = card.guess(guess)
        # Update the user's score based on the given guess
        user.change_score(correct_guess)

        # If the guess was correct
        if correct_guess == True:
            # Display Correct!
            #   with a whitespace on the end rather than a new line
            print("Correct!", end=" ")
        else:
            # Display Incorrect!
            #   with a whitespace on the end rather than a new line
            print("Incorrect!", end=" ")
        # Display the user's current score
        print(f"Your score is now {user.score}")

        # Check if the user has won
        if user.win():
            # Display winning message
            print(f"Your score is {user.score}")
            print("Congratulations! You have won the game! >.<")
            # End the game
            break
        # Check is the user has lost
        elif user.lose():
            # Display losing message
            print("You have lost the game. :(")
            # End the game
            break
        else:
            # Change the value of the card
            #   continue the loop
            card.next_card()


if __name__ == "__main__":
    main()
