from PIL import Image


def main():
    with Image.open("before1.jpg") as img:
        print(img.size)
        print(img.format)


main()