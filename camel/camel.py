### Convert camelCase into snake_case ###

def main():
    camel = input("camelCase: ")
    
    for i in camel:
        if i.isupper():
            snake_case = i.replace(i, "_" + i.lower())
            print(snake_case)    

main()