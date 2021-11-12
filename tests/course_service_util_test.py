import unittest

from app.adapters.http.util.courseServiceUtil import CourseServiceUtil
from fastapi.exceptions import HTTPException


class TestCourseServiceUtil(unittest.TestCase):

    def test_check_course_exists(self):
        course = CourseServiceUtil.check_course_exists(1)
        assert course is not None

    def test_check_course_not_exists(self):
        self.assertRaises(HTTPException, CourseServiceUtil.check_course_exists, 12412534266234)
