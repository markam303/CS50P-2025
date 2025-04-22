### Convert camelCase into snake_case ###

def main():
    camel = input("camelCase: ")
    
    snake = snake_case(camel)
    
    print(f"snake_case: {snake}")

def snake_case(camel):
    for i in camel:
        if i.isupper():
            camel = camel.replace(i, "_" + i.lower())  
    return camel


main()