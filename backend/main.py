# Main entry point to run FastAPI app

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from controllers.sales_rep_controller import api_router
from controllers.ai_controller import api_router as ai_router

app = FastAPI()
# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers from controllers
app.include_router(api_router)
app.include_router(ai_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
