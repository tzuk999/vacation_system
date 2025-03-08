from dal.base_dao import BaseDAO
from psycopg2.extras import RealDictCursor

class UsersDAO(BaseDAO):
    def __init__(self, connection_params, table_name, schema_name):
        super().__init__(connection_params, table_name, schema_name)

    #Ensure only users with role_id corresponding to 'user' can be added- excepting and adding User module data
    def add_user(self, data):
        if data.role_id != 2:
            raise ValueError("Only users with role 'user' can be added.")
        return self.add_row(data)
    
 # return a user by email and password
    def get_user_by_email_password(self, email:str, password:str):
        with self._get_connection() as conn:
            try:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(f"SELECT * FROM {self.schema_name}.{self.table_name} WHERE email = %s AND password = %s", (email, password))
                    return cur.fetchone()
            except:
                return False
    
 #  return TRUE if email exist, and FALSE if it doesnt
    def email_exists(self, email:str):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM {self.schema_name}.{self.table_name} WHERE email = %s", (email, ))
                if cur.fetchone():
                    return True
                else:
                    return False

 # adds like by user id and vacation id   
    def add_like(self, user_id:int, vacation_id:int):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO {self.schema_name}.likes (user_id, vacation_id) VALUES (%s, %s) ON CONFLICT DO NOTHING", (user_id, vacation_id))
                conn.commit()

 # removes like by user id and vacation id   
    def remove_like(self, user_id:int, vacation_id:int):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM {self.schema_name}.likes WHERE user_id = %s AND vacation_id = %s", (user_id, vacation_id))
                conn.commit()