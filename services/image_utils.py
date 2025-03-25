import os
import cv2
from datetime import datetime
from config import HISTORY_FOLDER


def save_image(img, suffix="raw"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{suffix}.jpg"
    path = os.path.join(HISTORY_FOLDER, filename)
    cv2.imwrite(path, img)
    return filename, path
