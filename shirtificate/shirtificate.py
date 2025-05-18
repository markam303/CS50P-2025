import fpdf
from PIL import Image


class PDF(fpdf.FPDF):
    def header(self):
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(20)


def main():
    pdf = fpdf.FPDF()
    pdf.add_page()
    background_image = Image.open("shirtificate.png")
    # pdf.allow_images_transparency = False
    pdf.image(background_image,
              h=pdf.eph,
              w=pdf.epw,
              alt_text="CS50 T-Shirt",
              )
    pdf.set_auto_page_break = False
    pdf.output("my-shirt.pdf")
    
...

if __name__ == "__main__":
    main()