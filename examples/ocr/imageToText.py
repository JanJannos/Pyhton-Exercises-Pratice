# First download an install the file from here (64 bit)
# https://github.com/UB-Mannheim/tesseract/wiki

import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def convert():
    img = Image.open("sample.png")
    text = pytesseract.image_to_string(img)
    print(text)

convert()