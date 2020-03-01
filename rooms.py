from converter import Converter
from db_manager import DbManager


class RoomDB:
    """Класс служит для работы с бд и сущностями Room"""
    def __init__(self, mysql_connector, data_mysql):
        self.db_manager = DbManager(mysql_connector, data_mysql)
        self.converter = Converter()
        self.create_table()
        self.create_index()

    def load_in_db(self, rooms: list) -> None:
        sql = """INSERT INTO rooms (id, name)
        VALUES (%s, %s)"""
        args = [(room["id"], room["name"]) for room in rooms]
        self.db_manager.execute_many(sql, args)

    def get_all(self) -> list:
        sql = """SELECT rooms.id, rooms.name, count(*) AS 'number_of_students'
        FROM rooms LEFT JOIN students ON rooms.id=students.room
        GROUP BY rooms.id"""
        result = self.db_manager.execute_query_with_result(sql)
        return self.converter.from_tuples_to_dicts_with_counter(result)

    def get_with_smallest_avg_age(self) -> list:
        sql = """SELECT rooms.id, rooms.name FROM rooms
        LEFT JOIN students ON rooms.id=students.room
        GROUP BY rooms.id
        ORDER BY AVG(((YEAR(CURRENT_DATE)-YEAR(birthday))-
        (DATE_FORMAT(CURRENT_DATE, '%m%d%hh%n%s') < DATE_FORMAT(birthday, '%m%d%hh%n%s'))))
        LIMIT 5"""
        result = self.db_manager.execute_query_with_result(sql)
        return self.converter.from_tuples_to_dicts(result)

    def get_with_the_biggest_difference_in_ages(self) -> list:
        sql = """SELECT rooms.id, rooms.name
        FROM rooms
        LEFT JOIN students ON rooms.id=students.room
        GROUP BY rooms.id
        ORDER BY (MAX(((YEAR(CURRENT_DATE)-YEAR(birthday))-
        (DATE_FORMAT(CURRENT_DATE, '%m%d%hh%n%s') <
        DATE_FORMAT(birthday, '%m%d%hh%n%s')))) -
        MIN(((YEAR(CURRENT_DATE)-YEAR(birthday))-
        (DATE_FORMAT(CURRENT_DATE, '%m%d%hh%n%s') <
        DATE_FORMAT(birthday, '%m%d%hh%n%s'))))) DESC
        LIMIT 5;"""
        result = self.db_manager.execute_query_with_result(sql)
        return self.converter.from_tuples_to_dicts(result)

    def get_with_heterosexuals(self) -> list:
        sql = """SELECT rooms.id, rooms.name
        FROM rooms
        LEFT JOIN students ON rooms.id=students.room
        GROUP BY rooms.id
        HAVING count(DISTINCT sex) = 1"""
        result = self.db_manager.execute_query_with_result(sql)
        return self.converter.from_tuples_to_dicts(result)

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS rooms(
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(100) NOT NULL)"""
        self.db_manager.execute_query(sql)

    def create_index(self):
        sql = "CREATE INDEX IX_Rooms ON rooms(id)"
        self.db_manager.execute_query(sql)
