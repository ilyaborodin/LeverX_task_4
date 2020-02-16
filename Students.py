from pymysql.err import IntegrityError
from collections import namedtuple


Student = namedtuple('Student', ['id', 'name', 'birthday', 'room', 'sex'])


class StudentDB:
    """Класс служит для работы с бд и сущностями типа Student"""
    def __init__(self, mysql_connector, data_mysql):
        self.MysqlConnector = mysql_connector
        self.data_mysql = data_mysql
        if not self.check_table():
            self.create_table()

    def load_in_db(self, students: list) -> None:
        with self.MysqlConnector(self.data_mysql) as db:
            for student in students:
                sql = "INSERT INTO students (id, name, birthday, sex, room)" \
                      " VALUES ({id}, '{name}', '{birthday}', '{sex}', {room})".format(id=student.id,
                                                                                name=student.name,
                                                                                birthday=student.birthday,
                                                                                sex=student.sex,
                                                                                room=student.room)
                try:
                    db.execute(sql)
                except IntegrityError:
                    continue

    def create_table(self):
        with self.MysqlConnector(self.data_mysql) as db:
            sql = 'CREATE TABLE students(' \
                  'id INTEGER PRIMARY KEY NOT NULL, ' \
                  'birthday DATETIME,' \
                  'name VARCHAR(100) NOT NULL,' \
                  'sex VARCHAR(1),' \
                  'room INTEGER,' \
                  'FOREIGN KEY (room) REFERENCES rooms(id))'
            db.execute(sql)

    def check_table(self):
        with self.MysqlConnector(self.data_mysql) as db:
            sql = 'show tables like \'students\''
            db.execute(sql)
            response = db.fetchone()
            table_is_created = response is not None and "students" in response
        return table_is_created