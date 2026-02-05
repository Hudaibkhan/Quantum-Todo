import sys
import os
# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db.session import settings
from src.api.tasks import router as tasks_router
from src.api.auth import router as auth_router
from src.middleware.auth import AuthMiddleware
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Evolution Todo API",
    description="RESTful API for Evolution Todo (Hackathon Phase II)",
    version="1.0.0"
)

# Include routers
app.include_router(auth_router, prefix="/api")
app.include_router(tasks_router, prefix="/api")

# CORS configuration
origins = [org.strip() for org in settings.CORS_ORIGINS.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add authentication middleware after CORS middleware
app.add_middleware(AuthMiddleware)

@app.on_event('startup')
async def startup_event():
    # This event will be used to initialize database connections
    logger.info("Application startup complete")

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, app_dir="./")