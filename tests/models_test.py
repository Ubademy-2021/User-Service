import unittest

from app.adapters.database.admins.model import AdminDTO
from app.adapters.database.favoriteCourses.model import FavoriteCourseDTO
from app.adapters.database.userCategories.model import UserCategoryDTO
from app.adapters.database.users.model import UserDTO
from app.domain.admins.model.admin import AdminBase
from app.domain.favoriteCourses.model.favoriteCourse import FavoriteCourse
from app.domain.userCategories.model.userCategory import UserCategory
from app.domain.users.model.user import UserCreate


def make_default_adminBase():
    adminCreate = AdminBase(
        email="aasdas",
        name="sdasdad",
        surname="fasfasd"
    )
    return adminCreate


def make_default_favoriteCourse():
    favoriteCourse = FavoriteCourse(
        userId=1,
        courseId=1
    )
    return favoriteCourse


def make_default_userCategory():
    userCategory = UserCategory(
        userId=1,
        categoryId=1
    )
    return userCategory


def make_default_userCreate():
    user = UserCreate(
        email="str",
        userName="str",
        name="str",
        surname="str",
        phoneNumber="str",
        city="str",
        state="str",
        country="str",
        address="str"
    )
    return user


class TestDatabaseModelsInit(unittest.TestCase):

    def test_admin_init(self):
        adminCreate = make_default_adminBase()
        assert adminCreate.isComplete()
        adminDTO = AdminDTO()
        adminDTO.initWithAdminCreate(adminCreate)
        assert adminDTO.email == adminCreate.email
        assert adminDTO.name == adminCreate.name
        assert adminDTO.surname == adminCreate.surname

    def test_favorite_course_init(self):
        favoriteCourse = make_default_favoriteCourse()
        favoriteCourseDTO = FavoriteCourseDTO()
        favoriteCourseDTO.initWithFavoriteCourse(favoriteCourse)
        assert favoriteCourseDTO.courseId == favoriteCourse.courseId
        assert favoriteCourseDTO.userId == favoriteCourse.userId

    def test_user_category_init(self):
        userCategory = make_default_userCategory()
        userCategoryDTO = UserCategoryDTO()
        userCategoryDTO.initWithUserCategory(userCategory)
        assert userCategoryDTO.categoryId == userCategory.categoryId
        assert userCategoryDTO.userId == userCategory.userId

    def test_user_init(self):
        user = make_default_userCreate()
        assert user.isComplete()
        userDTO = UserDTO()
        userDTO.initWithUserCreate(user)
        assert userDTO.address == user.address
        assert userDTO.city == user.city
        assert userDTO.country == user.country
        assert userDTO.email == user.email
        assert userDTO.name == user.name
        assert userDTO.surname == user.surname
        assert userDTO.userName == user.userName
        assert userDTO.phoneNumber == user.phoneNumber
        assert userDTO.state == user.state
        assert not userDTO.isBlock
