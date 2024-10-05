
import pyodbc
import datetime
import os
import shutil
import time
import threading
import cv2
import numpy
import glob
import sys
import subprocess

from ultralytics import YOLO
from dotenv import load_dotenv