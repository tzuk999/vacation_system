from dataclasses import dataclass

@dataclass
class UserDTO:
    id: int
    first_name: str
    last_name: str
    email: str
    role_id: int