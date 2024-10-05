
from imports import *


def detectTorpedo(detectModelPath, imagePath):
    detectModel = YOLO(detectModelPath)
    
    results = detectModel(imagePath)
    if not results("No bounding box"):
        return None
    
    for result in results:
        boxes = result.boxes
        if not boxes:
            print("No boxes found")
            return None
        
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().detach().numpy().astype(int)
            return x1, y1, x2, y2
    