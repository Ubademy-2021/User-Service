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

    def getAllCategories():
        logger.info("Getting all categories")

        url = HEROKU_COURSE_SERVICE_BASE_URL + "/api/categories/all/"
        r = requests.get(url=url)

        if r.status_code != 200:
            logger.warning("Request error: " + url)
            raise HTTPException(status_code=400, detail="Request error: " + url)

        # Return user
        return r.json()

    def getActiveCourses():
        logger.info("Getting all active courses")

        url = HEROKU_COURSE_SERVICE_BASE_URL + "/api/courses/active/"
        r = requests.get(url=url)

        if r.status_code != 200:
            logger.warning("Request error: " + url)
            raise HTTPException(status_code=400, detail="Request error: " + url)

        # Return user
        return r.json()

    def getCategoriesWithIds(ids: List):
        categories = CourseServiceUtil.getAllCategories()
        returnCategories = []
        for id in ids:
            for category in categories:
                if category["id"] == id:
                    returnCategories.append(category)
        return returnCategories

    def getCoursesWithIds(ids: List):
        courses = CourseServiceUtil.getActiveCourses()
        returnCourses = []
        for id in ids:
            for course in courses:
                if course["id"] == id:
                    returnCourses.append(course)
        return returnCourses
