
from imports import *

def findLatestImage(dir_path):
    image_extensions = ('*.jpg', '*.jpeg', '*.png')
    
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(dir_path)))
        
    if not image_files:
        print("No images found in the directory")
        return None
    
    latest_image = max(image_files, key=os.path.getatime)
    
    print(f"Latest Image: {latest_image}")
    
    return latest_image