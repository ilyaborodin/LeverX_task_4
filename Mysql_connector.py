import pymysql

data_mysql = {
    "host": "localhost",
    "user": "nonroot",
    "password": "Mysekret047",
    "db": "Task4",
}


class MysqlConnector:
    def __init__(self, mysql_data):
        self.connection = pymysql.connect(data_mysql)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.close()

    def open(self) -> None:
        self.connection.open()

    def close(self) -> None:
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def execute(self, sql):
        self.cursor.execute(sql)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.fetchall()
