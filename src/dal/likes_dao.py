from dal.base_dao import BaseDAO
import psycopg2
from psycopg2.extras import RealDictCursor

class LikesDAO(BaseDAO):
    def __init__(self, connection_params, table_name, schema_name):
        super().__init__(connection_params, table_name, schema_name)

# get like by user_id and vacation_id
    def get_like(self, user_id:int, vacation_id:int):
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(f"SELECT * FROM {self.schema_name}.{self.table_name} WHERE user_id = %s AND vacation_id = %s", (user_id, vacation_id))
                return cur.fetchone()
            

# adds like by user id and vacation id 
    def add_like(self, user_id:int, vacation_id:int):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO {self.schema_name}.{self.table_name} (user_id, vacation_id) VALUES (%s, %s) ON CONFLICT DO NOTHING", (user_id, vacation_id))
                conn.commit()


# removes like by user id and vacation id 
    def remove_like(self, user_id:int, vacation_id:int):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM {self.schema_name}.likes WHERE user_id = %s AND vacation_id = %s", (user_id, vacation_id))
                conn.commit()