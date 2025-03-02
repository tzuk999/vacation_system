from dal.base_dao import BaseDAO

class RolesDAO(BaseDAO):
    def __init__(self, connection_params,table_name, schema_name):
        super().__init__(connection_params, table_name, schema_name)