"""
CS50 P-Shirt. 
Provide input img as first CLA and name of output img as second CLA.
Possible extensions: jpg, jpeg, png.
"""

import sys
import os
import PIL


def main():
    # Check for CLA
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Extract extensions
    root, ext2 = os.path.splitext(sys.argv[2])
    root, ext1 = os.path.splitext(sys.argv[1])
    ext2 = ext2.lower()
    ext1 = ext1.lower()
    
    # Check for allowed extensions
    allowed_ext = [".jpg", ".jpeg", ".png"]
    if ext2 not in allowed_ext:
        sys.exit("Invalid output")
    elif ext1 not in allowed_ext:
        sys.exit("Invalid input")
    elif not ext1 == ext2:
        sys.exit("Input and output have different extensions")
        
    with PIL.Image.open(sys.argv[1]) as input:
        input = PIL.ImageOps.fit(input)
    
    with PIL.Image.open(sys.argv[2], "w") as output:
        output.paste()
        shirt = PIL.Image.open("shirt.png") 
        
        shirt.close()   


if __name__ == "__main__":
    main()