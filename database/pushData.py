
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

load_dotenv()

def pushData(torpedo_id, c_x, c_y, w, h, cam_id, filename):
    torpdeo_id = int(torpdeo_id)
    c_x = int(c_x)
    c_y = int(c_y)
    w = int(w)
    h = int(h)
    cam_id = int(cam_id)
    
    if (c_x > 200) and (c_y < 400):
        udt = 0
    else:
        udt = 2
        
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    
    conn_str = (
        f'DRIVER = {{ODBC Driver 17 for SQL Server}};'
        f'SERVER = {server};'
        f'DATABASE = {database};'
        f'UID = {username};'
        f'PWD = {password};'
    )
    
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    data = {
        "TorpedoID": torpedo_id,
        "detectiondttime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "centerx": c_x,
        "centery": c_y,
        "width": w,
        "height": h,
        "udt": udt,
        "CameraID": cam_id,
        "filename":filename
    }
    
    insert_query = """
    INSERT INTO torpedo_detection_master (TorpedoID, detectiondttime, centerx, centery, width, height, udt, CameraID)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    try:
        cursor.execute(insert_query, (
            data["TorpedoID"],
            data["detectiondttime"],
            data["centerx"],
            data["centery"],
            data["width"],
            data["height"],
            data["udt"],
            data["CameraID"],
            data["filename"]
        ))

        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
    
    