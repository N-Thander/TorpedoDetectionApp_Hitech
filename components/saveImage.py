
from imports import *

def saveImage(src, dst, TorpdeoID):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Cam1_{timestamp}_{TorpdeoID}.jpg"
        dst = os.path.join(dst_path, filename)

        shutil.copy2(src, dst)
        print(f"Image saved to {dst}")
        
    except Exception as e:
        print(f"Error: {e}")