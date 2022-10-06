from random import randint as r


class Card:

    def __init__(self):
        """Constructor for the Card class. Sets previous card value 
        (prev_value) and current card value (value) attributes to 0.\n
        Return: 
            None        
        """
        # Set the new attributes to a value of 0
        self.prev_value = 0
        self.value = 0

    def next_card(self):
        """Generates a random number between 0 and 100. Sets pre_value 
        to value. Sets value to the random number.\n
        Parameters:
            None
        Return:
            None
        """

        # Generate a random number between 0 and 100
        next_value = r(0, 13)

        # If the new number is equal to the previous number
        while next_value == self.prev_value:
            # Generate another random number between 0 and 100
            next_value = r(0, 13)

        # This is to keep track of the previous number so
        #   that next number wont be the same and for comparing
        #   higher or lower
        self.prev_value = self.value

        # Set the current card value to be the new random number
        self.value = next_value

    def guess(self, guess):
        """Compares the current card value to the previous card value, 
        and checks if the given guess is correct.\n
        Parameters:
            guess: The user's guess of higher (h) or lower (l)
        Return:
            True: If the guess is correct
            False: If the guess is incorrect
        """

        # If the user guessed higher and the current card value is higher
        #   than the previous card value
        if guess.lower() == "h" and self.value > self.prev_value:
            return True

        # If the user guessed lower and the current card value is lower
        #   than the previous card value
        elif guess.lower() == "l" and self.value < self.prev_value:
            return True

        # Else the guess is incorrect
        else:
            return False
