"""
CS50 P-Shirt. 
Provide input img as first CLA and name of output img as second CLA.
Possible extensions: jpg, jpeg, png.
"""

import sys
import os
from PIL import Image


def main():
    # Check for CLA
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check extensions
    root, ext = os.path.splitext(sys.argv[2])
    allowed_ext = [".jpg", ".jpeg", ".png"]


def extract_extension(text):
    os.path.splitext("text")


if __name__ == "__main__":
    main()