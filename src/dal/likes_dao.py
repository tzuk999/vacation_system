from dal.base_dao import BaseDAO

class LikesDAO(BaseDAO):
    def __init__(self, connection_params, table_name, schema_name):
        super().__init__(connection_params, table_name, schema_name)

    def get_like(self, user_id:int, vacation_id:int):
        pass