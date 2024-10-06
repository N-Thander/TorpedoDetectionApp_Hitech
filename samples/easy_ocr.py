
# testing easy ocr
# performance metrics < midocure > 

import easyocr
import cv2
import matplotlib.pyplot as plt

image_path = r"testing_images\\resized_frame00850.jpg"

reader = easyocr.Reader(['en']) 

img = cv2.imread(image_path)

results = reader.readtext(image_path)

numbers = []
for (bbox, text, prob) in results:
    if text.isdigit():  
        numbers.append(text)

print("Detected Numbers:", numbers)
