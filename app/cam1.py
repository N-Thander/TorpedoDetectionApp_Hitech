
from imports import *
from components.makeCopy import *
from components.deleteFiles import *
from components.clsTorpedo import *
from components.detectTorpedo import *
from components.findLatestImage import *
from components.calculateBBoxInfo import *

cam1_raw = ""

images_cam1 = "images_cam1"
temp_cam1 = "temp_cam1"

image_name = f"cam1_{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.jpg"

cls_model_path = "models\\cam1_classify.pt"
detection_model_path = "models\\cam1_detect.pt"


def cam1():
    deleteFiles(temp_cam1)
    makeCopy(cam1_raw, temp_cam1, image_name)
    
    image = findLatestImage(temp_cam1)
    
    isTorpedo = clsTorpedo(cls_model_path, image)
    
    if isTorpedo:
        x1, y1, x2, y2 = detectTorpedo(detection_model_path, image)
        c_x, c_y, w, h = calculateBBoxInfo(x1, y1, x2, y2)
        makeCopy(image, images_cam1, image_name)
        return c_x, c_y, w, h
    
    else:
        pass
    
    
    