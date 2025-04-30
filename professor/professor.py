### Little Professor: https://en.wikipedia.org/wiki/Little_Professor ###
import random


def main():
    level = get_level()
    score = 0
    for question in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        chance = 3
        
        while chance != 0:
            try:
                user_answer = int(input(f"{x} + {y} = "))    
                if answer == user_answer:
                    score += 1
                    print("Brawo!")
                    break
                else:
                    print("EEE")
                    chance -= 1
            except ValueError:
                print("EEE")
                chance -= 1
        if chance == 0:
            print("Answer:", answer)
    print("Score:", score)
    

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            
            if 1 <= level <= 3:
                return level
            else:
                pass
        except (ValueError, TypeError):
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()