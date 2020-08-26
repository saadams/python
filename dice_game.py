import random
import webbrowser

def guessRoll():
    guess = input('Guess a number between 1 and 6\n')
    guess.rstrip()
    guess=int(guess)
    if(guess >= 1 and guess <= 6):
        print(f"This is your guess {guess}.\n")
    else:
        print('please pick a number between 1 and 6.\n')
    return guess

def rollDice():
    roll = random.randrange(1,7)
    print("The dice is rolled...")
    print("---------------------")
    print(roll)
    return roll

def playGame(guess,roll):

    if(guess == roll):
        print('You guessed right')
    else:
        print("You guessed wrong")
        
    
playGame(guessRoll(),rollDice())