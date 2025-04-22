### Convert camelCase into snake_case ###

def main():
    camel = input("camelCase: ")
    
    for i in camel:
        if i.isupper():
            snake_case = camel.replace(i, "_" + i.lower())
            return snake_case    
        print(f"snake_case: {snake_case}") 
        return 0  
    
    print(f"snake_case: {camel}")

main()