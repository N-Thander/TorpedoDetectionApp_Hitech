
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from app.cam1 import *
from app.cam2 import *
from app.cam3 import *
from app.digitalCam import *
from app.rtspStreaming import *

from components.findLatestImageName import *

from database.pushData import *

torpedo_id = 99

images_digital = "images_digital"

images_cam1 = "images_cam1"
images_cam2 = "images_cam2"
images_cam3 = "images_cam3"

def cam1_thread_func():
    cam_id = 1
    c_x, c_y, w, h = cam1()
    
    if c_x == -99:
        print("No Detection")
    else:
        filename = findLatestImageName(images_cam1)
        pushData(torpedo_id, c_x, c_y, w, h, cam_id, filename)
        print("Cam1-data_pushed")

def cam2_thread_func():
    cam_id = 2
    c_x, c_y, w, h = cam2()
    
    if c_x == -99:
        print("No Detection")
    else:
        filename = findLatestImageName(images_cam2)
        pushData(torpedo_id, c_x, c_y, w, h, cam_id, filename)
        print("Cam2-data_pushed")
    

def cam3_thread_func():
    cam_id = 3
    c_x, c_y, w, h = cam3()
    
    if c_x == -99:
        print("No Detection")
    else:
        filename = findLatestImageName(images_cam3)
        pushData(torpedo_id, c_x, c_y, w, h, cam_id, filename)
        print('Cam3-Data pushed')


def main():
    rtspStreaming()
    
    digital_cam_result = digitalCam()
    
    if digital_cam_result:
        cam1_thread = threading.Thread(target=cam1_thread_func)
        cam2_thread = threading.Thread(target=cam2_thread_func)
        cam3_thread = threading.Thread(target=cam3_thread_func)
        
        cam1_thread.start()
        cam2_thread.start()
        cam3_thread.start()
        
        cam1_thread.join()
        cam2_thread.join()
        cam3_thread.join()
        
    else:
        ("No Torpedo In Frame")


if __name__ == "__main__":
    main()