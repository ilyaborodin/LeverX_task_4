import argparse
from environs import Env


class ArgsParser:
    """Класс служит для возврата аргументов с терминала"""
    def __init__(self):
        self.env = Env()
        self.data_mysql = None
        self.args = None
        self.get_db_args()
        self._set_args()

    def _set_args(self):
        parser = argparse.ArgumentParser(description='Command-line utility.')
        parser.add_argument('path_to_students', type=str, help='Path to students file')
        parser.add_argument('path_to_rooms', type=str, help='Path to rooms file')
        parser.add_argument('format', choices=['json', 'xml'], help='Output format')
        self.args = parser.parse_args()

    def get_args(self):
        return self.args.path_to_students, self.args.path_to_rooms,\
               self.args.format, self.data_mysql

    def get_db_args(self):
        self.env.read_env()
        with self.env.prefixed("MYSQL_"):
            self.data_mysql = {
                "host": self.env("HOST", None),
                "port": self.env("PORT", None),
                "user": self.env("USER", None),
                "password": self.env("PASSWORD", None),
                "db": self.env("DB", None)
            }
        if None in self.data_mysql.values():
            raise Exception("""Не все требуемые переменные окружения найдены.
Ожидаются: MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB""")
        if self.data_mysql["port"].isdigit():
            self.data_mysql["port"] = int(self.data_mysql["port"])
        else:
            raise Exception("Port должен содержать только цифры")
