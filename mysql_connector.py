import pymysql


class MysqlConnector:
    """Класс служит соединением с database"""
    def __init__(self, data_mysql):
        self.connection = self.get_connection(data_mysql)
        self.cursor = self.connection.cursor()
        self.cursor._defer_warnings = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.close()

    def get_connection(self, data_mysql):
        try:
            connection = pymysql.connect(host=data_mysql["host"], port=data_mysql["port"],
                                         user=data_mysql["user"], password=data_mysql["password"],
                                         db=data_mysql["db"])
        except pymysql.err.OperationalError:
            raise Exception("Введены неверные данные для подключения к бд")
        return connection

    def close(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def execute(self, sql):
        self.cursor.execute(sql)

    def execute_many(self, sql, args):
        self.cursor.executemany(sql, args)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def execute_with_result(self, sql):
        self.cursor.execute(sql)
        return self.fetchall()
