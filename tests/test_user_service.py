import unittest
from src.services.user_service import UserService
from src.dal.init_test_db import create_vacation_system_test_db
from src.config import db_connection_params

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.db_connection_params = db_connection_params
        create_vacation_system_test_db(self.db_connection_params)
        self.user_service = UserService(connection_params=self.db_connection_params, schema_name="test")

    def test_register_success(self):
        result = self.user_service.register("new.user@example.com", "pass1234", "New", "User")
        self.assertIsNone(result)  # Assuming successful registration prints a message

    def test_register_invalid_email(self):
        with self.assertRaises(ValueError):
            self.user_service.register("invalid-email", "pass1234", "John", "Doe")

    def test_login_success(self):
        user = self.user_service.login("john.doe@example.com", "password123")
        self.assertIsNotNone(user)

    def test_login_invalid_credentials(self):
        with self.assertRaises(ValueError):
            self.user_service.login("wrong@example.com", "wrongpass")

    def test_like_vacation_success(self):
        result = self.user_service.like_vacation(2, 1)  # User ID 2 (Jane Smith) likes Vacation ID 1
        self.assertIsNone(result)

    def test_like_vacation_invalid_user(self):
        with self.assertRaises(ValueError):
            self.user_service.like_vacation(999, 1)

    def test_unlike_vacation_success(self):
        result = self.user_service.unlike_vacation(2, 1)  # User ID 2 unlikes Vacation ID 1
        self.assertIsNone(result)

    def test_unlike_vacation_invalid_user(self):
        with self.assertRaises(ValueError):
            self.user_service.unlike_vacation(999, 1)

    def test_unlike_vacation_invalid_vacation(self):
        with self.assertRaises(ValueError):
            self.user_service.unlike_vacation(2, 999)


if __name__ == "__main__":
    unittest.main()
