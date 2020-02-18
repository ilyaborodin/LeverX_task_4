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
            for student in students:
                sql = """INSERT INTO students (id, name, birthday, sex, room)
                VALUES ({id}, '{name}', '{birthday}', '{sex}', {room})""".format(id=student.id,
                                                                                 name=student.name,
                                                                                 birthday=student.birthday,
                                                                                 sex=student.sex,
                                                                                 room=student.room)
                try:
                    db.execute(sql)
                except IntegrityError:
                    continue

    def create_table(self):
        with self.mysql_connector(self.data_mysql) as db:
            sql = """CREATE TABLE students(id INTEGER PRIMARY KEY NOT NULL,
            birthday DATETIME, name VARCHAR(100) NOT NULL,
            sex VARCHAR(1),
            room INTEGER,
            FOREIGN KEY (room) REFERENCES rooms(id))"""
            try:
                db.execute(sql)
            except InternalError:
                # print("Table 'rooms' already exists")
                pass

    def create_index(self):
        with self.mysql_connector(self.data_mysql) as db:
            sql = "CREATE INDEX IX_Students_room ON students(room, sex, birthday)"
            try:
                db.execute(sql)
            except InternalError:
                # print("Index IX_Students already exists")
                pass
