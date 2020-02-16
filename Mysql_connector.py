import pymysql

data_mysql = {
    "host": "localhost",
    "port": 3308,
    "user": "nonroot",
    "password": "Mysekret047",
    "db": "Task4",
}


class MysqlConnector:
    """Класс служит соединением с database"""
    def __init__(self, data_mysql):
        self.connection = pymysql.connect(host=data_mysql["host"], port=data_mysql["port"],
                                          user=data_mysql["user"], password=data_mysql["password"],
                                          db=data_mysql["db"])
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.close()

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
