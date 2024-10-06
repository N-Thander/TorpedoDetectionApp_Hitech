

from imports import *
from components.makeCopy import *
from components.deleteFiles import *
from components.clsTorpedo import *
from components.detectTorpedo import *
from components.findLatestImage import *
from components.calculateBBoxInfo import *

cam3_raw = ""

images_cam3 = "images_cam3"
temp_cam3 = "temp_cam3"

image_name = f"cam3_{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.jpg"

cls_model_path = "models\\cam3_classify.pt"
detection_model_path = "models\\cam3_detect.pt"


def cam3():
    deleteFiles(temp_cam3)
    makeCopy(cam3_raw, temp_cam3, image_name)
    
    image = findLatestImage(temp_cam3)
    
    isTorpedo = clsTorpedo(cls_model_path, image)
    
    if isTorpedo:
        x1, y1, x2, y2 = detectTorpedo(detection_model_path, image)
        c_x, c_y, w, h = calculateBBoxInfo(x1, y1, x2, y2)
        makeCopy(image, images_cam3, image_name)
        return c_x, c_y, w, h
    
    else:
        return None
    
    
    