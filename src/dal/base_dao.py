import psycopg2
from psycopg2.extras import RealDictCursor

class BaseDAO:
    def __init__(self, connection_params, table_name, schema_name):
        self.connection_params = connection_params
        self.table_name = table_name
        self.schema_name = schema_name
    def _get_connection(self):
        return psycopg2.connect(**self.connection_params)


    def read_all(self):
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(f"SELECT * FROM {self.schema_name}.{self.table_name}")
                return cur.fetchall()


    # getting a dictionery and adding a row to the table- keys = columns, values = valuse
    def add_row(self, data:dict):
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    f"INSERT INTO {self.schema_name}.{self.table_name} ({columns}) VALUES ({values}) RETURNING id",
                    tuple(data.values())
                )
                conn.commit()
                return cur.fetchone()[0]


    # reads a row by id
    def read_by_id(self, row_id):
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(f"SELECT * FROM {self.schema_name}.{self.table_name} WHERE id = %s", (row_id,))
                return cur.fetchone()


    # deleting a row by id
    def delete_by_id(self, row_id):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM {self.schema_name}.{self.table_name} WHERE id = %s", (row_id,))
                conn.commit()


    # updating a row by getting the row id and a dict of the columns and values
    def update_by_id(self, row_id, data:dict):
        set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
        
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"UPDATE {self.schema_name}.{self.table_name} SET {set_clause} WHERE id = %s",
                    tuple(data.values()) + (row_id,)
                )
                conn.commit()
