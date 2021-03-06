from pymysql.err import IntegrityError, InternalError
from typing import List, Tuple


class DbManager:
    def __init__(self, mysql_connector, data_mysql):
        self.mysql_connector = mysql_connector
        self.data_mysql = data_mysql

    def execute_query_with_result(self, sql: str):
        with self.mysql_connector(self.data_mysql) as db:
            return db.execute_with_result(sql)

    def execute_query(self, sql: str):
        with self.mysql_connector(self.data_mysql) as db:
            try:
                db.execute(sql)
            except (InternalError, IntegrityError):
                # print("Data already exists")
                pass

    def execute_many(self, sql: str, args: List[Tuple]):
        with self.mysql_connector(self.data_mysql) as db:
            try:
                db.execute_many(sql, args)
            except (InternalError, IntegrityError):
                # print("Data already exists")
                pass
