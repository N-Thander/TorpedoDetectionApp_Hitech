import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

def clsTorpedo(clsModePath, imagePath):
    clsModel = YOLO(clsModePath)
    
    results = clsModel.predict(source=imagePath)
    
    if not results:
        print("No result from Torpedo Model")
        return False
    
    for result in results:
        if hasattr(result, 'probs'):
            top1_class_id = result.probs.top1
            top1_confidence = result.probs.top1conf
            
            s = f"{top1_class_id} {result.names[top1_class_id]} {top1_confidence:.2f}"
            
            if "NonTorpedoFrame" in s:
                return False
        else:
            print("Result does not contain probability information")
    
    return True

