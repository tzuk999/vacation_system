from dal.base_dao import BaseDAO
from psycopg2.extras import RealDictCursor

class UsersDAO(BaseDAO):
    def __init__(self, connection_params, table_name):
        super().__init__(connection_params, table_name)

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
                    cur.execute("SELECT * FROM vacation_system.users WHERE email = %s AND password = %s", (email, password))
                    return cur.fetchone()
            except:
                raise ValueError("Email or Password are incorrect.")
    
 #  return 1 if email exist, and 0 if it doesnt
    def email_exists(self, email:str):
        with self._get_connection() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT COUNT(1) FROM vacation_system.users WHERE email = %s", (email,))
                    return cur.fetchone()[0]
            except:
                raise ValueError("Email doesn't exists.")
    
 # adds like by user id and vacation id   
    def add_like(self, user_id:int, vacation_id:int):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO vacation_system.likes (user_id, vacation_id) VALUES (%s, %s) ON CONFLICT DO NOTHING", (user_id, vacation_id))
                conn.commit()

 # removes like by user id and vacation id   
    def remove_like(self, user_id:int, vacation_id:int):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM vacation_system.likes WHERE user_id = %s AND vacation_id = %s", (user_id, vacation_id))
                conn.commit()