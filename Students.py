from Mysql_connector import MysqlConnector, data_mysql
from dataclasses import dataclass


@dataclass
class Student:
    birthday: str
    id: int
    name: str
    room: int
    sex: str


class StudentDB:
    def __init__(self, mysql_connector):
        self.mysql_connector = mysql_connector

    def load_in_db(self, students: list) -> None:
        pass
