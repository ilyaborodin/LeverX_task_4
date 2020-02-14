import pymysql


data_mysql = {
    "server": "localhost",
    "user": "nonroot",
    "password": "Mysekret047",
    "database": "Task4",
}


class MysqlConnector:
    def __init__(self, mysql_data):
        self.con = self._make_connector(self, mysql_data)

    def __call__(self, *args, **kwargs):
        return self.con

    def _make_connector(self, mysql_data):
        con = pymysql.connect(mysql_data["server"],
                              mysql_data["nonroot"],
                              mysql_data["password"],
                              mysql_data["database"], )
        return con

    def open(self) -> None:
        self.con.open()

    def close(self) -> None:
        self.con.close()

