
from imports import *

def makeCopy(src, dst_path, filename):
    try:
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        
        dst_file = os.path.join(dst_path, filename)
        shutil.copy2(src, dst_path)
        
        print(f"file copied succesfully to {dst_path} with name {dst_file}")
        
    except Exception as e:
        print(f"Error occured while copying file: {e}")
        pass