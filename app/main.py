import os
import uvicorn
import logging
from fastapi import FastAPI, status
from app.adapters.http.users import users_controller
from app.adapters.database.users.model import Base
from app.adapters.database.database import engine

Base.metadata.create_all(bind=engine)

# Create app with FAST API
app = FastAPI(debug=True)

logging.info("Starting User-Service")


@app.get('/ping', status_code=status.HTTP_200_OK)
async def root():
    logging.warn("This is an testing endpoint, not intended for productive environment")
    return "pong"


app.include_router(users_controller.router, prefix="/api")

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    logging.info("Using port: " + port)
    uvicorn.run(app, host='0.0.0.0', port=port)
