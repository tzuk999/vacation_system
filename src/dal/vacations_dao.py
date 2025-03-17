from src.dal.base_dao import BaseDAO

class VacationsDAO(BaseDAO):
    def __init__(self, connection_params, table_name, schema_name):
        super().__init__(connection_params, table_name, schema_name)


    #get all vacation in order by starting date
    def getAllVacations(self):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM {self.schema_name}.{self.table_name} ORDER BY start_date ASC")
                return cur.fetchall()