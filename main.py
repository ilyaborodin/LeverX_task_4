from Mysql_connector import MysqlConnector, data_mysql
from Rooms import RoomDB, RoomConverter
from Students import StudentDB
from FileReader import JSONReader
from DataExporter import DataExporter
from ArgsParser import ArgsParser


def main():
    args_parser = ArgsParser()
    room_db = RoomDB(MysqlConnector, data_mysql)
    student_db = StudentDB(MysqlConnector, data_mysql)
    json_reader = JSONReader()
    data_exporter = DataExporter()
    path_to_students, path_to_rooms, format_of_output = args_parser.get_args()
    rooms = json_reader.get_rooms(path_to_rooms)
    room_db.load_in_db(rooms)
    students = json_reader.get_students(path_to_students)
    student_db.load_in_db(students)
    all_rooms = room_db.get_all()
    data_exporter.export_to(all_rooms, format_of_output, "all_rooms_with_counter")


if __name__ == '__main__':
    main()
