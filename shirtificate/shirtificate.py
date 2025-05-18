import fpdf



class PDF(fpdf.FPDF):
    def header(self):
        # Setting font:
        self.set_font("helvetica", style="B", size=40)
        # Printing title:
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)


def main():
    name = get_name()
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(False)
    
    pdf.image("shirtificate.png",
              h=pdf.eph,
              w=pdf.epw,
              alt_text="CS50 T-Shirt",
              keep_aspect_ratio=True,
              )
    
    pdf.set_y(pdf.eph / 2)
    pdf.set_font("Times", style="B", size=28)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    
    pdf.output("my-shirt.pdf")
    
    

def get_name():
    return input("What's your name? ")


if __name__ == "__main__":
    main()