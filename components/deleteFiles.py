
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

def deleteFiles(dir_path):
    try:
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                
            
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                elif os.path.isdir(file_path):
                    print(f"Skipping directory: {file_path}")
                
            print("All files in the directory have been deleted.")
            
        else:
            print("Invalid directory path")
        
    except Exception as e:
        print(f"An error occured: {e}")