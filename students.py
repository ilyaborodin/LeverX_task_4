from pymysql.err import IntegrityError, InternalError
from collections import namedtuple


Student = namedtuple('Student', ['id', 'name', 'birthday', 'room', 'sex'])


class StudentDB:
    """Класс служит для работы с бд и сущностями типа Student"""
    def __init__(self, mysql_connector, data_mysql):
        self.mysql_connector = mysql_connector
        self.data_mysql = data_mysql
        self.create_table()

    def load_in_db(self, students: list) -> None:
        with self.mysql_connector(self.data_mysql) as db:
            sql = """INSERT INTO students (id, name, birthday, sex, room)
            VALUES (%s, %s, %s, %s, %s)"""
            args = [(student.id, student.name, student.birthday, student.sex, student.room) for student in students]
            try:
                db.execute_many(sql, args)
            except IntegrityError:
                # print("Data in table 'students' already exists")
                pass

    def create_table(self):
        with self.mysql_connector(self.data_mysql) as db:
            sql = """CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY NOT NULL,
            birthday DATETIME, name VARCHAR(100) NOT NULL,
            sex VARCHAR(1),
            room INTEGER,
            FOREIGN KEY (room) REFERENCES rooms(id))"""
            db.execute(sql)

    def create_index(self):
        with self.mysql_connector(self.data_mysql) as db:
            sql = "CREATE INDEX IX_Students_room ON students(room, sex, birthday)"
            try:
                db.execute(sql)
            except InternalError:
                # print("Index IX_Students already exists")
                pass
