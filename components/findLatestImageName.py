
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

def findLatestImageName(dir_path):
    image_extensions = ('*.jpg', '*.jpeg', '*.png')  
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(dir_path, ext)))
    
    if not image_files:
        print("No images found in the directory")
        return None
    
    latest_image = max(image_files, key=os.path.getatime)
    
    return os.path.basename(latest_image)