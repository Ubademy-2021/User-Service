import os

import uvicorn
from fastapi import FastAPI, status

from app.adapters.database.database import engine
from app.adapters.database.users.model import Base
from app.adapters.http.admins import admins_controller
from app.adapters.http.categories import categories_controller
from app.adapters.http.favoriteCourses import favoriteCoursesController
from app.adapters.http.users import users_controller
from app.core.logger import logger

Base.metadata.create_all(bind=engine)


# Create app with FAST API
app = FastAPI(debug=True)

logger.info("Starting User-Service")


@app.get('/ping', status_code=status.HTTP_200_OK)
async def root():
    logger.warning("This is an testing endpoint, not intended for productive environment")
    return "pong"


app.include_router(users_controller.router, prefix="/api")
app.include_router(categories_controller.router, prefix="/api")
app.include_router(admins_controller.router, prefix="/api")
app.include_router(favoriteCoursesController.router, prefix="/api")

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    logger.info("Using port: " + port)
    uvicorn.run(app, host='0.0.0.0', port=port)
