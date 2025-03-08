from dal.users_dao import UsersDAO
from models.user_dto import UserDTO
from dal.vacations_dao import VacationsDAO
import re

class UserService:
    def __init__(self, connection_params, schema_name):
        self.user_dao = UsersDAO(connection_params, "users", schema_name)
        self.vacation_dao = VacationsDAO(connection_params, "vacations", schema_name)


    #checking the all the required values exists and are fit to the requirements, if they do, adding a user with a role type of user- role_id-2
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
        if self.user_dao.add_user(user_data):
            print(f"user {user_data['first_name']} {user_data['last_name']} added successfully")

    
   #gets email and password - checking that they are stand in the requirements, than trying to fetch a user by them- return UserDTO object 
    def login(self, email: str, password: str):
        if not email or not password:
            raise ValueError("Email and password are required")
        
        if not re.match(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            raise ValueError("Invalid email format")
        
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long")
        
        try:
            user_data = self.user_dao.get_user_by_email_password(email, password)
            if user_data:
                user = UserDTO(id= user_data["id"], first_name= user_data["first_name"], last_name= user_data["last_name"], email= user_data["email"], role_id= user_data["role_id"])
                print(f'{user.first_name} logged in succesfuly')
                return user
            else:
                raise ValueError("Invalid email or password")
        except Exception as e:
            raise Exception("Database error") from e


    # getting user and vacation id, checking that the user and the vacation exist and adding a like
    def like_vacation(self, user_id: int, vacation_id: int):
        if not self.user_dao.read_by_id(user_id):
            raise ValueError("User does not exist")
        
        if not self.vacation_dao.read_by_id(vacation_id):
            raise ValueError("Vacation does not exist")
    
        try:
            self.user_dao.add_like(user_id, vacation_id)
            print(f'added like by user- {user_id} to vacation- {vacation_id}')
        except Exception as e:
            raise Exception("Database error") from e
        


    # getting user and vacation id, checking that the user and the vacation exist and deleting a like if it exists
    def unlike_vacation(self, user_id: int, vacation_id: int):
        if not self.user_dao.read_by_id(user_id):
            raise ValueError("User does not exist")
        
        if not self.vacation_dao.read_by_id(vacation_id):
            raise ValueError("Vacation does not exist")
        
        
        try:
            self.user_dao.remove_like(user_id, vacation_id)
            print(f'removed like by user- {user_id} to vacation- {vacation_id}')
        except Exception as e:
            raise Exception("Database error") from e
