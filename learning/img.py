from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("before1.jpg") as img:
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("edged.jpg")

main()