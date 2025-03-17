import unittest
from datetime import date
from src.services.vacation_service import VacationService
from src.dal.init_test_db import create_vacation_system_test_db
from src.config import db_connection_params


class TestVacationService(unittest.TestCase):
    def setUp(self):
        self.db_connection_params = db_connection_params
        create_vacation_system_test_db(self.db_connection_params)
        self.vacation_service = VacationService(connection_params=self.db_connection_params, schema_name="test")


    def test_add_vacation_success(self):
        result = self.vacation_service.add_vacation(1, "Road trip in Texas", date(2025, 7, 1), date(2025, 7, 10), 1800, "texas.jpg")
        self.assertIsNotNone(result)


    def test_add_vacation_invalid_price(self):
        with self.assertRaises(ValueError):
            self.vacation_service.add_vacation(1, "Budget trip", date(2025, 6, 1), date(2025, 6, 10), -10, "budget.jpg")


    def test_update_vacation_success(self):
        result = self.vacation_service.update_vacation(1, 2, "Updated trip", date(2025, 8, 1), date(2025, 8, 10), 2000, "updated.jpg")
        self.assertIsNone(result)


    def test_update_vacation_invalid(self):
        with self.assertRaises(Exception):
            self.vacation_service.update_vacation(1, 2, "Invalid trip", date(2025, 8, 10), date(2025, 8, 1), 2000, "invalid.jpg")


    def test_delete_vacation_success(self):
        result = self.vacation_service.delete_vacation(1)
        self.assertIsNone(result)


    def test_delete_vacation_invalid_id(self):
        with self.assertRaises(Exception):
            self.vacation_service.delete_vacation(999)

if __name__ == "__main__":
    unittest.main()
