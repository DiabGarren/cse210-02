import random as r 


def main(): 
    return(guess)

print("""To play the game is very simple, you will start with 300 points. To begin you will be shown a card at random. You will need
to guess whether you think the next card will be higher in value or lower. Guess right and you earn 100 points. Guess wrong and you 
will lose 75. Reach 1,000 points and you win the game, reach 0 and you lose. 
Good luck!""")

card_value = r.randint(1,13)

guess = str(input("Please enter whether you think the next card will be higher or lower. (h/l)\n").lower())
#need to add where the program initiates the game by saying the card value is x



def hilo_game():
    return r.randint(card_value)

keep_playing = True
has_points = True

while keep_playing: 
    keep_playing = str(input("Would you like to keep playing? (y/n)\n").lower())

    if has_points < 0: 
        keep_playing()

    elif has_points > 1000: 
        str(input("You have won the game. Would you like to play again? (y/n)\n").lower())

    else: 
        str(input("You have lost the game. Would you like to play again? (y/n)\n").lower())
#program does not quit when you click no 



def calculation():
    return(player_score)

player_score = []
x = 300

#trying to create a list where the original score of 300 is kept, and after each round the score is appended, and displays the current score til they either each 1,000 and win or 0 and lose
while guessing:
    if guess > card_value:
        for i in range (1, 1000): 
            x -= 75
            player_score.append(x)
            print("Too high, you lose 75 points. ")
            print("Current score = {player_score}." )

    elif guess < card_value:
        for i in range (1, 1000): 
            x -= 75
            player_score.append(x)
            print("Too low, you lose 75 points. ")
            print("Current score = {player_score}." )

    else:
        for i in range (1, 1000):
            x += 100
            player_score.append(x)
            print("Nice, you got it! You earned 100 points. ")
            print("Current score = {player_score}." )
            guessing = False





if __name__ == "main":
    main()

