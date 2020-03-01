from pymysql.err import IntegrityError, InternalError
from collections import namedtuple
from db_manager import DbManager

Student = namedtuple('Student', ['id', 'name', 'birthday', 'room', 'sex'])


class StudentDB:
    """Класс служит для работы с бд и сущностями типа Student"""

    def __init__(self, mysql_connector, data_mysql):
        self.db_manager = DbManager(mysql_connector, data_mysql)
        self.create_table()
        self.create_index()

    def load_in_db(self, students: list) -> None:
        sql = """INSERT INTO students (id, name, birthday, sex, room)
            VALUES (%s, %s, %s, %s, %s)"""
        args = [(student.id, student.name, student.birthday, student.sex, student.room) for student in students]
        self.db_manager.execute_many(sql, args)

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY NOT NULL,
        birthday DATETIME, name VARCHAR(100) NOT NULL,
        sex VARCHAR(1),
        room INTEGER,
        FOREIGN KEY (room) REFERENCES rooms(id))"""
        self.db_manager.execute_query(sql)

    def create_index(self):
        sql = "CREATE INDEX IX_Students_room ON students(room, sex, birthday)"
        self.db_manager.execute_query(sql)
