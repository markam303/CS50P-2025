import numpy as np
from PIL import Image 
import csv


def main():
    with open("views.csv", "r", encoding='UTF-8') as file, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()
        
        for row in reader:
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"), 2)
            writer.writerow()

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness
    
    
main()