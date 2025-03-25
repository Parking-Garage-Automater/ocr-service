from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import numpy as np
import cv2
from services.ocr import extract_number
from services.mqtt import publish
from config import MQTT_TOPIC, MQTT_MESSAGE
from services.image_utils import save_image

router = APIRouter()


@router.post("/process-label/{gate}")
async def process_gate_image(gate: str, request: Request):
    image_bytes = await request.body()
    img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    raw_filename, _ = save_image(img, "raw")

    raw_text, processed, number = extract_number(img)
    gate_opened = False

    if number:
        publish(MQTT_TOPIC, MQTT_MESSAGE)
        save_image(processed, f"{number}_proc")
        gate_opened = True

    return JSONResponse({
        "raw_text": raw_text,
        "number": number,
        "gate_opened": gate_opened
    })
