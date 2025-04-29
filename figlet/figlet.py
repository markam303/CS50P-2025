### Transforming text into Figlet ###
from pyfiglet import Figlet
import random
import sys


figlet = Figlet()
f = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(f)
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in f:
            f = sys.argv[2] 
        else:    
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")          
else:
    sys.exit("Invalid usage")


figlet.setFont(font=f)
s = input("Input: ")
print("Output:\n", figlet.renderText(s))