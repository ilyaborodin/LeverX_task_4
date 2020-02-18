from mysql_connector import MysqlConnector
from rooms import RoomDB
from students import StudentDB
from file_reader import JsonReader
from data_exporter import JsonExporter, XmlExporter
from args_parser import ArgsParser
from converter import Converter


def main():
    args_parser = ArgsParser()
    path_to_students, path_to_rooms, format_of_output, data_mysql = args_parser.get_args()
    converter = Converter()
    room_db = RoomDB(MysqlConnector, data_mysql)
    student_db = StudentDB(MysqlConnector, data_mysql)
    json_reader = JsonReader()

    json_rooms = json_reader.load_json_file(path_to_rooms)
    rooms = converter.from_list_to_rooms(json_rooms)
    room_db.load_in_db(rooms)

    json_students = json_reader.load_json_file(path_to_students)
    students = converter.from_list_to_students(json_students)
    student_db.load_in_db(students)

    if format_of_output == "json":
        data_exporter = JsonExporter()
    else:
        data_exporter = XmlExporter()

    all_rooms = room_db.get_all()
    all_rooms_output = converter.from_namedtuples_to_dicts_with_counter(all_rooms)
    data_exporter.export(all_rooms_output, "[1]all_rooms_with_counter")

    avg_rooms = room_db.get_with_smallest_avg_age()
    avg_rooms_output = converter.from_namedtuples_to_dicts(avg_rooms)
    data_exporter.export(avg_rooms_output, "[2]rooms_with_smallest_avg_age")

    rooms_with_big_delta = room_db.get_with_the_biggest_difference_in_ages()
    rooms_with_big_delta_output = converter.from_namedtuples_to_dicts(rooms_with_big_delta)
    data_exporter.export(rooms_with_big_delta_output, "[3]rooms_with_the_biggest_difference_in_ages")

    rooms_with_heterosexuals = room_db.get_with_heterosexuals()
    rooms_with_heterosexuals_output = converter.from_namedtuples_to_dicts(rooms_with_heterosexuals)
    data_exporter.export(rooms_with_heterosexuals_output, "[4]rooms_with_heterosexuals")


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(str(error))
