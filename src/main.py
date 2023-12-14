import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import general_settings
from routes import router

app = FastAPI(
    title="Subnetting API",
    description="API for IP segmentation and subnetting",
    version="0.0.1",
)

origins = ["http://localhost", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    HOST = general_settings.HOST
    PORT = general_settings.PORT
    DEBUG = general_settings.DEBUG
    APP_NAME = general_settings.APP_NAME
    uvicorn.run(app=APP_NAME, host=HOST, port=PORT, reload=DEBUG)
