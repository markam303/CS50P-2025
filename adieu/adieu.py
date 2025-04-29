### Adieu, adieu! ###
import inflect


def main():
    count = 0
    names = []
    
    while True:
        try:
            name = input("Name: ")    
            names.append(name)    
            count += 1
        except EOFError:
            break
        
    p = inflect.engine()    
    print("Adieu, adieu, to ", end="")
    print(p.join((names), final_sep=","))
    
if __name__ == "__main__":
    main()