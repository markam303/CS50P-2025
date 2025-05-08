"""
CS50 P-Shirt. 
Provide input img as first CLA and name of output img as second CLA.
Possible extensions: jpg, jpeg, png.
"""

import sys
import os
from PIL import Image, ImageOps


def main():
    # Check for CLA
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Extract extensions
    input_extension = os.path.splitext(sys.argv[1])[1].lower()
    output_extension = os.path.splitext(sys.argv[2])[1].lower()
    
    # Check for allowed extensions
    allowed_ext = [".jpg", ".jpeg", ".png"]
    if output_extension not in allowed_ext:
        sys.exit("Invalid output")
    elif input_extension not in allowed_ext:
        sys.exit("Invalid input")
    elif not input_extension == output_extension:
        sys.exit("Input and output have different extensions")
    
    # Overlay input image with shirt image and produce output image
    shirt = Image.open("shirt.png") 
    size_shirt = shirt.size  
     
    try:
        with Image.open(sys.argv[1]) as input:
            input = ImageOps.fit(input, size_shirt)
            output = Image.new("RGB", size_shirt)
            output = input
            output.paste(shirt, shirt)
            output.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
    shirt.close()


if __name__ == "__main__":
    main()