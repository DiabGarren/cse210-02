import random as r 

def main(): 
    """ To play the game is very simple, you will start with 300 points. To begin you will be shown a card at random. You will need
to guess whether you think the next card will be higher in value or lower. Guess right and you earn 100 points. Guess wrong and you 
will lose 75. Reach 1,000 points and you win the game, reach 0 and you lose. 
Good luck! 
"""
range = r.randint(1,13) #set between 1 and 13 because cards only have value between 1 and 13
running_total = 0

while running_total < 1000:
    print("Will the next card be higher or lower? ")

    if running_total == 1000:
        print("Congrats, you won the game! ")

    else: 
        answer = input("Would you like to play again? Yes or No. ")
        if answer == 'yes': 
            if answer == 'no':
                quit

    def store_calculations(): 
        turn = int(answer)
        calculations = calculations + turn 
        print("You have {} points currently. ")


if __name__ == "main":
    main()

