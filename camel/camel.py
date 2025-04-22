### Convert camelCase into snake_case ###

def main():
    camel = input("camelCase: ")
    
    for i in camel:
        if i.isupper():
            i = i.replace(i, "_" + i.lower())
            print(camel)    

main()