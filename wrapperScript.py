
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

def wrapperScript():
    while True:
        try:
            process = subprocess.Popen(['python', 'main.py'])
            process.wait()
            
        except Exception as e:
            print(f"Error running main.py: {e}")
            
        finally:
            time.sleep(2)
            
if __name__ == "__main__":
    wrapperScript()