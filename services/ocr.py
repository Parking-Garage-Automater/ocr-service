import cv2
import numpy as np
import easyocr

reader = easyocr.Reader(['en'])


def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.flip(gray, 1)
    filtered = cv2.bilateralFilter(gray, 11, 17, 17)
    thresh = cv2.adaptiveThreshold(
        filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 9)
    kernel = np.ones((2, 2), np.uint8)
    return cv2.dilate(thresh, kernel, iterations=1)


def extract_number(img):
    processed = preprocess_image(img)
    results = reader.readtext(processed, detail=0)
    for text in results:
        if text.strip().isdigit() and len(text.strip()) == 4:
            return results, processed, text.strip()
    return results, processed, None
