from dal.users_dao import UsersDAO
from dal.vacations_dao import VacationsDAO
import re

class UserService:
    def __init__(self):
        self.user_dao = UsersDAO()
        self.vacation_dao = VacationsDAO()

    def register(self, email: str, password: str, first_name: str, last_name: str):
        if not email or not password or not first_name or not last_name:
            raise ValueError("All fields are required")
        
        if not re.match(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            raise ValueError("Invalid email format")
        
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long")
        
        if self.user_dao.email_exists(email):
            raise ValueError("Email already exists in the system")
        
        user_data = {'email': email, 'password': password, 'first_name': first_name, 'last_name': last_name, 'role_id': 2}
        return self.user_dao.add_user(user_data)

    def login(self, email: str, password: str):
        if not email or not password:
            raise ValueError("Email and password are required")
        
        if not re.match(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            raise ValueError("Invalid email format")
        
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long")
        
        user = self.user_dao.get_user_by_email_password(email, password)
        if not user or user.password != password:
            raise ValueError("Invalid email or password")
        
        return user

    def like_vacation(self, user_id: int, vacation_id: int):
        if not self.user_dao.read_by_id(user_id):
            raise ValueError("User does not exist")
        
        if not self.vacation_dao.read_by_id(vacation_id):
            raise ValueError("Vacation does not exist")
    
        return self.user_dao.add_like(user_id, vacation_id)

    def unlike_vacation(self, user_id: int, vacation_id: int):
        if not self.user_dao.read_by_id(user_id):
            raise ValueError("User does not exist")
        
        if not self.vacation_dao.read_by_id(vacation_id):
            raise ValueError("Vacation does not exist")
        
        
        return self.user_dao.remove_like(user_id, vacation_id)
