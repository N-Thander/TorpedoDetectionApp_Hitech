import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

RTSP_URL = ""

save_dir = "images_rtsp\\"
filename = "rtsp_image.jpg"

save_path = os.path.join(save_dir, filename)

cap = cv2.VideoCapture(RTSP_URL)

def rtspStreaming():
    if not cap.isOpened():
        print("Error: Could not open stream")
        return
    try:
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print("Error: Failed to grab Frame.")
                break
            
            cv2.imwrite(save_path, frame)
            cv2.imshow('RTSP Steam', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()