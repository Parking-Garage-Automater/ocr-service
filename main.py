from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import gates, images, dashboard

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gates.router)
app.include_router(images.router)
app.include_router(dashboard.router)
