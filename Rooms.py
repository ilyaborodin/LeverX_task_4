from dataclasses import dataclass


@dataclass
class Room:
    id: int
    name: str


class RoomDB:
    def __init__(self, mysql_connector, data_mysql):
        self.MysqlConnector = mysql_connector
        self.data_mysql = data_mysql
        if not self.check_table():
            self.create_table()

    def load_in_db(self, rooms: list) -> None:
        pass

    def get_all(self) -> list:
        pass

    def get_with_smallest_avg_age(self) -> list:
        pass

    def get_with_biggest_difference_in_ages(self) -> list:
        pass

    def get_with_heterosexuals(self) -> list:
        pass

    def create_table(self):
        with self.MysqlConnector(self.data_mysql) as db:
            sql = 'CREATE TABLE rooms(' \
                  'id INTEGER PRIMARY KEY NOT NULL, ' \
                  'name VARCHAR(100) NOT NULL)'
            db.execute(sql)

    def check_table(self):
        with self.MysqlConnector(self.data_mysql) as db:
            sql = 'show tables like \'rooms\''
            db.execute(sql)
            response = db.fetchone()
            table_is_created = response is not None and "rooms" in response
        return table_is_created
