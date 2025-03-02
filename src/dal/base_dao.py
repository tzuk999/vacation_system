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

    def add_row(self, data):
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"INSERT INTO {self.schema_name}.{self.table_name} ({columns}) VALUES ({values}) RETURNING id",
                    tuple(data.values())
                )
                conn.commit()
                return cur.fetchone()[0]

    def read_by_id(self, row_id):
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(f"SELECT * FROM {self.schema_name}.{self.table_name} WHERE id = %s", (row_id,))
                return cur.fetchone()

    def delete_by_id(self, row_id):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM {self.schema_name}.{self.table_name} WHERE id = %s", (row_id,))
                conn.commit()
