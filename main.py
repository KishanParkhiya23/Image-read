# ocr_utils.py

from PIL import Image
import numpy as np
import pytesseract

def extract_text_from_image(image_path):
    input_image = Image.open(image_path)
    input_array = np.array(input_image)
    output_image = Image.fromarray(input_array)

    raw_text = pytesseract.image_to_string(output_image)
    cleaned_text = raw_text.replace("-", "").replace("=", "")
    return cleaned_text


image_path = str("image.png")
docketData = extract_text_from_image(image_path)
print(docketData)