
from imports import *

def makeCopy(src, dst_path):
    try:
        shutil.copy2(src, dst_path)
    except Exception as e:
        pass