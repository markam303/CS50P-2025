import fpdf
from PIL import Image


def main():
    pdf = fpdf.FPDF()
    pdf.add_page()
    background_image = pdf.image("shirtificate.png")
    pdf.allow_images_transparency = False
    pdf.set_page_background(background_image)
    pdf.set_auto_page_break = False
    pdf.output("my-shirt.pdf")
    
...

if __name__ == "__main__":
    main()