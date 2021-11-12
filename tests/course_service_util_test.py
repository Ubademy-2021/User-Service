import unittest

from app.adapters.http.util.courseServiceUtil import CourseServiceUtil
from fastapi.exceptions import HTTPException


class TestCourseServiceUtil(unittest.TestCase):

    def test_check_course_exists(self):
        course = CourseServiceUtil.check_course_exists(1)
        assert course

    def test_check_course_not_exists(self):
        self.assertRaises(HTTPException, CourseServiceUtil.check_course_exists, 12412534266234)

    def test_check_category_exists(self):
        category = CourseServiceUtil.check_category_exists(1)
        assert category

    def test_check_category_not_exists(self):
        self.assertRaises(HTTPException, CourseServiceUtil.check_category_exists, 121241252352512)

    def test_get_categories(self):
        categories = CourseServiceUtil.getCategoriesWithIds([1, 2])
        assert len(categories) == 2

    def test_get_courses(self):
        courses = CourseServiceUtil.getCoursesWithIds([1, 2, 4])
        assert len(courses) == 2
