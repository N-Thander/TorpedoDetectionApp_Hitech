
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


stream_images_cam1 = "testing_images\cam2.jpg"
images_cam1 = "images_cam1"
temp_cam1 = "temp_cam1"

cls_model_path_cam1 = ""
detect_model_path_cam1 = ""

temp_filename = f"temp_cam1.jpg"
final_filename = f"cam1_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"

def cam1():
    deleteFiles(temp_cam1)
    makeCopy(stream_images_cam1, temp_cam1, temp_filename)
    temp_image_cam1 = findLatestImagePath(temp_cam1)
    torpedoInframe = clsTorpedo(cls_model_path_cam1, temp_image_cam1)
    
    if torpedoInframe:
        x1, y1, x2, y2 = detectTorpedo(detect_model_path_cam1, temp_cam1)
        
        if x1 == None:
            print("Detect Torpedo Returned None")
            return -99, -99, -99, -99
        else:
            saveImage(temp_image_cam1, images_cam1, final_filename)
            c_x, c_y, w, h = calculateBBoxInfo(x1, y1, x2, y2)
            return c_x, c_y, w, h
    