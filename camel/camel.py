### Convert camelCase into snake_case ###

def main():
    camel = input("camelCase: ")
    
    for i in camel:
        if i.isupper():
            snake_case = camel.replace(i, "_" + i.lower())    
            print(f"snake_case: {snake_case}")   

main()