
from imports import *
from components.clsTorpedo import *
from components.makeCopy import *
from components.deleteFiles import *
from components.findLatestImage import *

rtsp_streaming_image = "images\\digital_image.jpg"

temp_digital = "temp_digital"
images_digital = "images_digital"

clsModelPath =  "models\digitalcam_cls.pt"

save_image_name = f"digitalcam_{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.jpg"

def digitalCam():
    deleteFiles(temp_digital)
    makeCopy(rtsp_streaming_image, temp_digital, save_image_name)
    digital_image_path = findLatestImage(temp_digital)
    isTorpedo = clsTorpedo(clsModelPath, digital_image_path)
    
    if isTorpedo:
        makeCopy(digital_image_path, images_digital, save_image_name)
        return isTorpedo
    else:
        return None
    
    