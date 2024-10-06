
from imports import *

from app.cam1 import *
from app.cam2 import *
from app.cam3 import *
from app.digitalCam import *
from app.directionOfMotion import *
from app.ocr import *

from database.pushData import *

from components.findLatestImage import *

udt = 0

image_cam1 = "images_cam1"
image_cam2 = "images_cam2"
images_cam3 = "images_cam3"

torpedo_id = 100

def cam1_thread_func():
    cam_id = 1
    
    result = cam1()
    
    if result == "-99":
        print('Returned no bounding box')
        pass
    else:
        c_x, c_y , w, h = result
        cam1_image_path = findLatestImage(image_cam1)
        cam1_image = os.path.basename(cam1_image_path)
        # insert_detection_data(torpedo_id, c_x, c_y, w, h, cam_id, cam1_image)
        print("Cam1 Data Pushed")
    
    
def cam2_thread_func():
    pass


def cam3_thread_func():
    pass


def main():
    isTorpedo = digitalCam()
    
    if isTorpedo:
        cam1_thread = threading.Thread(target=cam1_thread_func)
        # cam2_thread = threading.Thread(target=cam2_thread_func)
        # cam3_thread = threading.Thread(target=cam3_thread_func)
        
        cam1_thread.start()
        # cam2_thread.start()
        # cam3_thread.start()
        
        cam1_thread.join
        # cam2_thread.join
        # cam3_thread.join
    else:
        print("No Torpedo in Current Frame")

if __name__ == "__main__":
    main()