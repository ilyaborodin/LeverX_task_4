from pymysql.err import IntegrityError, InternalError
from collections import namedtuple
from converter import Converter


Room = namedtuple('Room', ['id', 'name'])


class RoomDB:
    """Класс служит для работы с бд и сущностями Room"""
    def __init__(self, mysql_connector, data_mysql):
        self.mysql_connector = mysql_connector
        self.data_mysql = data_mysql
        self.converter = Converter()
        self.create_table()
        self.create_index()

    def load_in_db(self, rooms: list) -> None:
        with self.mysql_connector(self.data_mysql) as db:
            for room in rooms:
                sql = """INSERT INTO rooms (id, name)
                VALUES ({id}, '{name}')""".format(id=room.id, name=room.name)
                try:
                    db.execute(sql)
                except IntegrityError:
                    continue

    def get_all(self) -> list:
        with self.mysql_connector(self.data_mysql) as db:
            sql = """SELECT rooms.id, rooms.name, count(*) AS 'number_of_students'
            FROM rooms LEFT JOIN students ON rooms.id=students.room
            GROUP BY rooms.id"""
            result = db.query(sql)
        return self.converter.from_tuples_to_rooms_with_counter(result)

    def get_with_smallest_avg_age(self) -> list:
        with self.mysql_connector(self.data_mysql) as db:
            sql = """SELECT rooms.id, rooms.name FROM rooms
            LEFT JOIN students ON rooms.id=students.room
            GROUP BY rooms.id
            ORDER BY AVG(((YEAR(CURRENT_DATE)-YEAR(birthday))-
            (DATE_FORMAT(CURRENT_DATE, '%m%d%hh%n%s') < DATE_FORMAT(birthday, '%m%d%hh%n%s'))))
            LIMIT 5"""
            result = db.query(sql)
        return self.converter.from_tuples_to_rooms(result)

    def get_with_the_biggest_difference_in_ages(self) -> list:
        with self.mysql_connector(self.data_mysql) as db:
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
            result = db.query(sql)
        return self.converter.from_tuples_to_rooms(result)

    def get_with_heterosexuals(self) -> list:
        with self.mysql_connector(self.data_mysql) as db:
            sql = """SELECT rooms.id, rooms.name
            FROM rooms
            LEFT JOIN students ON rooms.id=students.room
            GROUP BY rooms.id
            HAVING count(DISTINCT sex) = 1"""
            result = db.query(sql)
        return self.converter.from_tuples_to_rooms(result)

    def create_table(self):
        with self.mysql_connector(self.data_mysql) as db:
            sql = """CREATE TABLE rooms(
            id INTEGER PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL)"""
            try:
                db.execute(sql)
            except InternalError:
                # print("Table 'rooms' already exists")
                pass

    def create_index(self):
        with self.mysql_connector(self.data_mysql) as db:
            sql = "CREATE INDEX IX_Rooms ON rooms(id)"
            try:
                db.execute(sql)
            except InternalError:
                # print("Index IX_Rooms already exists")
                pass
