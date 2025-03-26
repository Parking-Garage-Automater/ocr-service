from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes import gates, images, dashboard
from midleware.dependencies import verify_api_key


app = FastAPI(dependencies=[Depends(verify_api_key)], root_path="/ocr")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gates.router)
app.include_router(images.router)
app.include_router(dashboard.router)
