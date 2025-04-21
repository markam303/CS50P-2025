### Math interpreter: input formua as X Y Z ###

expression = input("Expression: ").strip()

x, y, z = expression.split(" ")
x = int(x)
z = int(z)
match y:
    case "+":
        print(round(x + z, 1))    
    case "-":
        print(round(x - z, 1)) 
    case "*":
        print(round(x * z, 1))   
    case "/":
        print(round(x / z, 1))     
        
