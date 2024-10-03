# cam1

from imports import *


temp_cam1 = ""
save_directory = ""

cam1_image_path = ""
cam1_temp_image = ""

torpedo_classify_cam1 = ""
torpedo_detect_cam1 = ""

clsModel = YOLO(torpedo_classify_cam1)
detectModel = YOLO(torpedo_detect_cam1)

def makeCopy():
    src_image = cam1_image_path
    dst_path = temp_cam1
    try:
        shutil.copy2(src_image, dst_path)
    except Exception as e:
        print(f"Error: {e}")

def saveImage(TorpdeoID):
    src = cam1_temp_image  # Your source image path
    dst_path = save_directory  # Directory where you want to save the image

    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Cam1_{timestamp}_{TorpdeoID}.jpg"
        dst = os.path.join(dst_path, filename)

        shutil.copy2(src, dst)
        print(f"Image saved to {dst}")
        
    except Exception as e:
        print(f"Error: {e}")

def clsTorpedo():
    results = clsModel.predict(source=cam1_image_path)
    if not results:
        print("No result from torpedo Model")
        return False
    for result in results:
        top1_class_id = result.probs.top1
        top1_confidence = result.probs.top1conf
        s = f"{top1_class_id} {result.names[top1_class_id]}{top1_confidence: .2f}"
        if "NonTorpedoFrame" in s:
            return False
    return True
        


def detectObject():
    largest_area = 0
    results = detectModel(cam1_image_path)
    if not results:
        return None
    
    for result in results:
        boxes = result.boxes
        if not boxes:
            return None
        for box in boxes:
            x1, y1, x2, y2, = box.xyxy[0].cpu().detach().numpy().astype(int)
            width = x2 - x1
            height = y2 - y1
            
            area = width * height
            
            if area > largest_area:
                largest_box = (x1, y1, x2, y2, width, height)
                largest_area = area
                
    return largest_box
            
            
def calculateBBoxInfo(x1, y1, x2, y2):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    
    return center_x, center_y
            
            
            
            
            
            
            
            
            
            
            
            
            