from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes import gates, images, dashboard
from middleware.dependencies import verify_api_key
from middleware.limiter import limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware


app = FastAPI(dependencies=[Depends(
    verify_api_key)], root_path="/ocr")
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.add_exception_handler(
    RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(gates.router)
app.include_router(images.router)
app.include_router(dashboard.router)
