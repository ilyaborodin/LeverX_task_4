from mysql_connector import MysqlConnector, data_mysql
from rooms import RoomDB, RoomConverter
from students import StudentDB
from file_reader import JsonReader
from data_exporter import DataExporter
from args_parser import ArgsParser


def main():
    args_parser = ArgsParser()
    room_db = RoomDB(MysqlConnector, data_mysql)
    student_db = StudentDB(MysqlConnector, data_mysql)
    json_reader = JsonReader()
    data_exporter = DataExporter()
    path_to_students, path_to_rooms, format_of_output = args_parser.get_args()
    rooms = json_reader.get_rooms(path_to_rooms)
    room_db.load_in_db(rooms)
    students = json_reader.get_students(path_to_students)
    student_db.load_in_db(students)

    all_rooms = room_db.get_all()
    data_exporter.export_to(all_rooms, format_of_output, "[1]all_rooms_with_counter")

    avg_rooms = room_db.get_with_smallest_avg_age()
    data_exporter.export_to(avg_rooms, format_of_output, "[2]rooms_with_smallest_avg_age")

    rooms_with_big_delta = room_db.get_with_the_biggest_difference_in_ages()
    data_exporter.export_to(rooms_with_big_delta, format_of_output, "[3]rooms_with_the_biggest_difference_in_ages")

    rooms_with_heterosexuals = room_db.get_with_heterosexuals()
    data_exporter.export_to(rooms_with_heterosexuals, format_of_output, "[4]rooms_with_heterosexuals")


if __name__ == '__main__':
    main()
