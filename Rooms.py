from pymysql.err import IntegrityError, InternalError
from collections import namedtuple


Room = namedtuple('Room', ['id', 'name'])


class RoomDB:
    """Класс служит для работы с бд и сущностями Room"""
    def __init__(self, mysql_connector, data_mysql):
        self.MysqlConnector = mysql_connector
        self.data_mysql = data_mysql
        self.room_converter = RoomConverter()
        self.create_table()
        # self.create_index()

    def load_in_db(self, rooms: list) -> None:
        with self.MysqlConnector(self.data_mysql) as db:
            for room in rooms:
                sql = "INSERT INTO rooms (id, name)" \
                      " VALUES ({id}, '{name}')".format(id=room.id, name=room.name)
                try:
                    db.execute(sql)
                except IntegrityError:
                    continue

    def get_all(self) -> list:
        with self.MysqlConnector(self.data_mysql) as db:
            sql = "SELECT rooms.id, rooms.name, count(*) AS 'number_of_students' " \
                "FROM rooms JOIN students ON rooms.id=students.room " \
                "GROUP BY rooms.id, rooms.name"
            result = db.query(sql)
        return self.room_converter.convert_to_dicts_from_id_name_number(result)

    def get_with_smallest_avg_age(self) -> list:
        with self.MysqlConnector(self.data_mysql) as db:
            sql = "SELECT rooms.id, rooms.name FROM rooms " \
                  "JOIN students ON rooms.id=students.room " \
                  "GROUP BY rooms.id, rooms.name " \
                  "ORDER BY AVG(((YEAR(CURRENT_DATE)-YEAR(birthday))-" \
                  "(DATE_FORMAT(CURRENT_DATE, '%m%d%hh%n%s') < DATE_FORMAT(birthday, '%m%d%hh%n%s')))) " \
                  "LIMIT 5"
            result = db.query(sql)
        return self.room_converter.convert_to_dicts_from_id_name(result)

    def get_with_the_biggest_difference_in_ages(self) -> list:
        with self.MysqlConnector(self.data_mysql) as db:
            sql = "SELECT rooms.id, rooms.name " \
                  "FROM rooms " \
                  "JOIN students ON rooms.id=students.room " \
                  "GROUP BY rooms.id, rooms.name " \
                  "ORDER BY (MAX(((YEAR(CURRENT_DATE)-YEAR(birthday))-" \
                  "(DATE_FORMAT(CURRENT_DATE, '%m%d%hh%n%s') < " \
                  "DATE_FORMAT(birthday, '%m%d%hh%n%s')))) - " \
                  "MIN(((YEAR(CURRENT_DATE)-YEAR(birthday))-" \
                  "(DATE_FORMAT(CURRENT_DATE, '%m%d%hh%n%s') < " \
                  "DATE_FORMAT(birthday, '%m%d%hh%n%s'))))) DESC " \
                  "LIMIT 5;"
            result = db.query(sql)
        return self.room_converter.convert_to_dicts_from_id_name(result)

    def get_with_heterosexuals(self) -> list:
        with self.MysqlConnector(self.data_mysql) as db:
            sql = "SELECT id, name " \
                  "FROM (SELECT rooms.id, rooms.name, count(DISTINCT sex) as 'count' " \
                  "FROM rooms JOIN students ON rooms.id=students.room " \
                  "GROUP BY rooms.id, rooms.name) as T " \
                  "where count=1"
            result = db.query(sql)
        return self.room_converter.convert_to_dicts_from_id_name(result)

    def create_table(self):
        with self.MysqlConnector(self.data_mysql) as db:
            sql = 'CREATE TABLE rooms(' \
                  'id INTEGER PRIMARY KEY NOT NULL, ' \
                  'name VARCHAR(100) NOT NULL)'
            try:
                db.execute(sql)
            except InternalError:
                # print("Table 'rooms' already exists")
                pass

    def create_index(self):
        with self.MysqlConnector(self.data_mysql) as db:
            sql = "CREATE INDEX IX_Rooms ON rooms(id, name)"
            try:
                db.execute(sql)
            except IntegrityError:
                pass


class RoomConverter:
    """Класс преобразует информацию с бд в dicts для того, чтобы в будущем сохранить в json/xml файлы"""
    def convert_to_dicts_from_id_name_number(self, tuple_of_rooms: tuple) -> list:
        dicts = []
        for tuple_of_room in tuple_of_rooms:
            dicts.append(dict(id=tuple_of_room[0],
                              name=tuple_of_room[1],
                              number_of_students=tuple_of_room[2]))
        return dicts

    def convert_to_dicts_from_id_name(self, tuple_of_rooms: tuple) -> list:
        dicts = []
        for tuple_of_room in tuple_of_rooms:
            dicts.append(dict(id=tuple_of_room[0],
                              name=tuple_of_room[1]))
        return dicts
