from mysql_connector import MysqlConnector
from rooms import RoomDB
from students import StudentDB
from file_reader import JsonReader
from data_exporter import JsonExporter, XmlExporter
from args_parser import ArgsParser


def main():
    args_parser = ArgsParser()
    path_to_students, path_to_rooms, format_of_output, data_mysql = args_parser.get_args()
    room_db = RoomDB(MysqlConnector, data_mysql)
    student_db = StudentDB(MysqlConnector, data_mysql)
    json_reader = JsonReader()

    rooms = json_reader.load_json_file(path_to_rooms)
    room_db.load_in_db(rooms)

    students = json_reader.load_json_file(path_to_students)
    student_db.load_in_db(students)

    if format_of_output == "json":
        data_exporter = JsonExporter()
    else:
        data_exporter = XmlExporter()

    all_rooms = room_db.get_all()
    data_exporter.export(all_rooms, "[1]all_rooms_with_counter")

    avg_rooms = room_db.get_with_smallest_avg_age()
    data_exporter.export(avg_rooms, "[2]rooms_with_smallest_avg_age")

    rooms_with_big_delta = room_db.get_with_the_biggest_difference_in_ages()
    data_exporter.export(rooms_with_big_delta, "[3]rooms_with_the_biggest_difference_in_ages")

    rooms_with_heterosexuals = room_db.get_with_heterosexuals()
    data_exporter.export(rooms_with_heterosexuals, "[4]rooms_with_heterosexuals")


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(str(error))
