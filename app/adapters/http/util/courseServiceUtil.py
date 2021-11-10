from typing import List

from fastapi.exceptions import HTTPException
from app.core.config import HEROKU_COURSE_SERVICE_BASE_URL
import requests
from app.core.logger import logger


class CourseServiceUtil:

    def check_course_exists(id):
        logger.info("Checking if course with id: " + str(id) + " exists")

        url = HEROKU_COURSE_SERVICE_BASE_URL + "/api/courses/" + str(id)
        r = requests.get(url=url)

        if r.status_code != 200:
            logger.warning("Course not found")
            raise HTTPException(status_code=400, detail="Course does not exist")

        # Return user
        return r.json()

    def check_category_exists(id):
        logger.info("Checking if category with id: " + str(id) + " exists")

        url = HEROKU_COURSE_SERVICE_BASE_URL + "/api/categories/" + str(id)
        r = requests.get(url=url)

        if r.status_code != 200:
            logger.warning("Category not found")
            raise HTTPException(status_code=400, detail="Category does not exist")

        # Return user
        return r.json()
