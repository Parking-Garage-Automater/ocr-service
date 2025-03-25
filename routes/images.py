# routes/images.py
import os
import glob
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, Response
from config import HISTORY_FOLDER

router = APIRouter()


@router.get("/image")
def get_latest_processed_image():
    """Return the latest processed image (_proc.jpg)"""
    image_files = glob.glob(os.path.join(HISTORY_FOLDER, "*_proc.jpg"))
    if not image_files:
        return Response(content="No processed image found", status_code=404)

    latest_image = max(image_files, key=os.path.getmtime)
    return FileResponse(latest_image, media_type="image/jpeg")


@router.get("/image/{filename}")
def get_image_by_filename(filename: str):
    """Return image by filename if exists"""
    path = os.path.join(HISTORY_FOLDER, filename)
    if os.path.exists(path):
        return FileResponse(path, media_type="image/jpeg")
    raise HTTPException(status_code=404, detail="Image not found")
