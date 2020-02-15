from Mysql_connector import MysqlConnector, data_mysql
from dataclasses import dataclass


@dataclass
class Student:
    id: int
    name: str
    birthday: str
    room: int
    sex: str


class StudentDB:
    def __init__(self, mysql_connector, data_mysql):
        self.MysqlConnector = mysql_connector
        self.data_mysql = data_mysql
        if not self.check_table():
            self.create_table()

    def load_in_db(self, students: list) -> None:
        pass

    def create_table(self):
        with self.MysqlConnector(self.data_mysql) as db:
            sql = 'CREATE TABLE students(' \
                  'id INTEGER PRIMARY KEY NOT NULL, ' \
                  'birthday DATETIME,' \
                  'name VARCHAR(100) NOT NULL,' \
                  'sex VARCHAR(1),' \
                  'room INTEGER,' \
                  'FOREIGN KEY (room) REFERENCES rooms(id))'
            db.execute(sql)

    def check_table(self):
        with self.MysqlConnector(self.data_mysql) as db:
            sql = 'show tables like \'students\''
            db.execute(sql)
            response = db.fetchone()
            table_is_created = response is not None and "students" in response
        return table_is_created