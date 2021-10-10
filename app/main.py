import os
import uvicorn
from fastapi import FastAPI, status
from app.adapters.http.users import users_controller
from app.adapters.database.users.model import Base
from app.adapters.database.database import engine
from app.core.logger import logger

Base.metadata.create_all(bind=engine)


# Create app with FAST API
app = FastAPI(debug=True)

logger.info("Starting User-Service")


@app.get('/ping', status_code=status.HTTP_200_OK)
async def root():
    logger.warn("This is an testing endpoint, not intended for productive environment")
    return "pong"


app.include_router(users_controller.router, prefix="/api")

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    logger.info("Using port: " + port)
    uvicorn.run(app, host='0.0.0.0', port=port)
