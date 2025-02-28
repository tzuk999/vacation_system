from dal.base_dao import BaseDAO

class UsersDAO(BaseDAO):
    def __init__(self, connection_params, table_name):
        super().__init__(connection_params, table_name)

    """Ensure only users with role_id corresponding to 'user' can be added."""
    def add_user(self, data):
        if data.get("role_id") != 2:  # Assuming '2' is the ID for 'user'
            raise ValueError("Only users with role 'user' can be added.")
        return self.add_row(data)
