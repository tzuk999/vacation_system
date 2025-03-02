from dal.base_dao import BaseDAO

class VacationsDAO(BaseDAO):
    def __init__(self, connection_params, table_name, schema_name):
        super().__init__(connection_params, table_name, schema_name)