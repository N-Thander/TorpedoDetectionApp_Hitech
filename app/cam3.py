
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

from components.calculateBBoxInfo import *
from components.clsTorpedo import *
from components.deleteFiles import *
from components.detectTorpedo import *
from components.clsTorpedo import *
from components.findLatestImageName import *
from components.findLatestImagePath import *
from components.makeCopy import *
from components.saveImage import *

stream_images_cam3 = ""

images_cam3 = ""
temp_cam3 = ""

cls_model_path_cam3 = ""
detect_model_path_cam3 = ""

temp_filename = f"temp_cam3.jpg"
final_filename = f"cam3_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"

def cam3():
    deleteFiles(temp_cam3)
    makeCopy(stream_images_cam3, temp_cam3, temp_cam3)
    temp_image_cam3 = findLatestImagePath(temp_cam3)
    torpeodInframe = clsTorpedo(cls_model_path_cam3, temp_cam3)
    
    if torpeodInframe:
        x1, y1, x2, y2 = detectTorpedo(detect_model_path_cam3, temp_cam3)
        
        if x1 == None:
            print("Detect Torpedo Returned None")
            return -99, -99, -99, -99
        else:
            saveImage(temp_image_cam3, images_cam3, final_filename)
            c_x, c_y, w, h = calculateBBoxInfo(x1, y1, x2, y2)
            return c_x, c_y, w, h
    