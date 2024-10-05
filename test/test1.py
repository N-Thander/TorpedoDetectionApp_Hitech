
# ocr testing 

import cv2
import numpy as np
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

image_path = "testing_images\\resized_frame00850.jpg"
img = cv2.imread(image_path)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# gray = cv2.erode(gray, None, iterations=1)
# gray = cv2.dilate(gray, None, iterations=1)
# _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


processed_img = Image.fromarray(img)

custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
text = pytesseract.image_to_string(processed_img, config=custom_config)

print("Extracted Numbers:", text)