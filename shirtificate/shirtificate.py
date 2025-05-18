import fpdf



class PDF(fpdf.FPDF):
    def header(self):
        # Setting font:
        self.set_font("helvetica", style="B", size=40)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)


def main():
    pdf = PDF()
    pdf.add_page()

    pdf.image("shirtificate.png",
              h=pdf.eph,
              w=pdf.epw,
              alt_text="CS50 T-Shirt",
              keep_aspect_ratio=True,
              )
    
    pdf.output("my-shirt.pdf")
    pdf.set_auto_page_break(False)
    

def get_name():
    return input("What's your name? ")


if __name__ == "__main__":
    main()