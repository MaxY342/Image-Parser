from PIL import Image
from pytesseract import pytesseract


def parseImage(imagePath):
    pathToTesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = pathToTesseract
    # Open the image file
    img = Image.open(imagePath)
    # Use pytesseract to parse the image
    text = pytesseract.image_to_string(img)
    with open("output.txt", "w") as f:
        f.write(text)

parseImage(r"images\captch.png")