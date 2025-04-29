### Guessing Game: guess number between 1 and 100 ###
import random
import sys


def main():
    while True:
        level = get_level()
        random.seed()
        try:
            answer = random.randint(1, level)
            break
        except ValueError:
            pass

    while True:
        guess = get_guess()
        if answer > guess:
            print("Too small!")
            pass
        elif answer < guess:
            print("Too large!")
            pass
        else:
            sys.exit("Just right!")
            


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            return level
        except (ValueError, TypeError):
            pass        
        except level < 1:
            pass

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            return guess
        except (ValueError, TypeError):
            pass
        except guess < 1:
            pass

    
if __name__ == "__main__":
    main()