
from imports import *

temp_cam2 = ""
save_directory = ""

cam2_image_path = ""
cam2_temp_image = ""

torpedo_classify_cam2 = ""
torpedo_detect_cam2 = ""


clsModel = YOLO(torpedo_classify_cam2)
detectModel = YOLO(torpedo_detect_cam2)

def makeCopy():
    src