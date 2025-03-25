import os
import glob
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from config import HISTORY_FOLDER

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def index():
    image_files = sorted(
        glob.glob(os.path.join(HISTORY_FOLDER, "*_proc.jpg")),
        key=os.path.getmtime,
        reverse=True
    )

    if not image_files:
        return HTMLResponse("<h2>No images yet.</h2>")

    grid_html = ""
    for path in image_files:
        filename = os.path.basename(path)
        parts = filename.split("_")

        timestamp = f"{parts[0]} {parts[1]}" if len(parts) >= 3 else "Unknown"
        number = parts[2] if len(parts) >= 3 else "Unknown"

        grid_html += f"""
        <div style="border:1px solid #ccc; padding:10px; margin:10px; width:220px;">
            <img src="/image/{filename}" style="width:200px;"/><br/>
            <strong>Time:</strong> {timestamp}<br/>
            <strong>Number:</strong> {number}<br/>
            <a href="/image/{filename}" download>Download</a>
        </div>
        """

    return f"""
    <html>
    <head><title>Image Dashboard</title></head>
    <body>
        <h1>All Detected Labels</h1>
        <div style="display:flex; flex-wrap:wrap;">
            {grid_html}
        </div>
        <a href="/history">View raw image history</a>
    </body>
    </html>
    """


@router.get("/history", response_class=HTMLResponse)
def history():
    image_files = sorted(
        glob.glob(os.path.join(HISTORY_FOLDER, "*.jpg")),
        key=os.path.getmtime,
        reverse=True
    )

    if not image_files:
        return HTMLResponse("<h2>No history available.</h2>")

    links = ""
    for path in image_files:
        filename = os.path.basename(path)
        links += f'<li><a href="/image/{filename}" download>{filename}</a></li>'

    return f"""
    <html>
    <head><title>Image History</title></head>
    <body>
        <h1>Download Image History</h1>
        <ul>
            {links}
        </ul>
        <a href="/">Back to dashboard</a>
    </body>
    </html>
    """
