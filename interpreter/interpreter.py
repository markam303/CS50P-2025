### Math interpreter: input formua as X Y Z ###

expression = input("Expression: ").strip()

x, y, z = expression.split(" ")
x = float(x)
z = float(z)
match y:
    case "+":
        print(round(x + z))    
    case "-":
        print(round(x - z)) 
    case "*":
        print(round(x * z))   
    case "/":
        print(round(x / z))     
        
