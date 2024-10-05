

def calculateBBoxInfo(x1, y1, x2, y2):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    
    width = x2 - x1
    height = y2 - y1
    
    return center_x, center_y, width, height
            