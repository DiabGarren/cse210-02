class User:

    def __init__(self):
        """Constructor for the User class. Sets user's score (score)
        attribute to 1.\n
        Return: 
            None 
        """
        self.score = 1
    
    def change_score(self, guess):
        """Checks if the user's guess was correct, and adjusts the 
        score accordingly. If the guess was correct, add 100 points.
        If the guess was incorrect, subtract 75 points.\n
        Parameters:
            guess: True or False, based on the user's guess
        Return:
            None
        """

        # Check if the guess was correct
        if guess == True:
            # Add 100 points
            self.score += 100

        # If the guess was incorrect
        else:
            # Subtract 75 points
            self.score -= 75
    
    def win(self):
        """If the user has more than 1000 points, then the user 
        wins.\n
        Parameters:
            None
        Return:
            True: If the user has more than 1000 points
            False: If the user has less than 1000 points
        """

        # If the current score is greater than or equal to 1000 points
        if self.score >= 1000:
            return True
        else:
            return False
    
    def lose(self):
        """If the user has less than 0 points, then the user 
        loses.\n
        Parameters:
            None
        Return:
            True: If the user has less than 0 points
            False: If the user has has than 0 points
        """

        # If the current score is less than or equal to 0 points
        if self.score <= 0:
            return True
        else:
            return False