import numpy as np
from PIL import Image 
import csv


def main():
    with open("views.csv") as file, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()
        
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            print(round(brightness, 2))

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness
    
    
main()