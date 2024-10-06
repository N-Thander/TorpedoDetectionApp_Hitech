
from imports import *
from components.makeCopy import *
from components.deleteFiles import *
from components.clsTorpedo import *
from components.detectTorpedo import *
from components.findLatestImage import *
from components.calculateBBoxInfo import *

cam2_raw = "images\\cam2.jpg"

images_cam2 = "images_cam2"
temp_cam2 = "temp_cam2"

image_name = f"cam2_{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.jpg"

cls_model_path = "models\\cam2_classify.pt"
detection_model_path = "models\\cam2_detect.pt"


def cam2():
    deleteFiles(temp_cam2)
    makeCopy(cam2_raw, temp_cam2, image_name)
    
    image = findLatestImage(temp_cam2)
    
    isTorpedo = clsTorpedo(cls_model_path, image)
    
    if isTorpedo:
        x1, y1, x2, y2 = detectTorpedo(detection_model_path, image)
        c_x, c_y, w, h = calculateBBoxInfo(x1, y1, x2, y2)
        makeCopy(image, images_cam2, image_name)
        return c_x, c_y, w, h
    
    else:
        return None
    
    
    