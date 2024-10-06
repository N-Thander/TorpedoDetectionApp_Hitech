
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

from components.clsTorpedo import *
from components.deleteFiles import *
from components.findLatestImageName import *
from components.findLatestImagePath import *
from components.makeCopy import *
from components.saveImage import *

rtsp_stream = "testing_images\digital_image.jpg"

images_digital = "images_digital"
digital_temp = "temp_digital"

temp_filename = f"temp_digitalImage.jpg"
final_filename = f"digitalCam_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"

cls_model_path = "models\digitalcam_cls.pt"

def digitalCam():
    deleteFiles(digital_temp)
    makeCopy(rtsp_stream, digital_temp, temp_filename)
    temp_image_path = findLatestImagePath(digital_temp)
    isTorpedo = clsTorpedo(cls_model_path, temp_image_path)
    if isTorpedo:
        saveImage(temp_image_path, images_digital, final_filename)
        return True
    else:
        return False
