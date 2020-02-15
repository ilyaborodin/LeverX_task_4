from Mysql_connector import MysqlConnector, data_mysql


class Room:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class RoomDB:
    def __init__(self, mysql_connector):
        self.mysql_connector = mysql_connector

    def load_in_db(self, Rooms: list) -> None:
        pass

    def get_all(self) -> list:
        pass

    def get_with_smallest_avg_age(self) -> list:
        pass

    def get_with_biggest_difference_in_ages(self) -> list:
        pass

    def get_with_heterosexuals(self) -> list:
        pass
