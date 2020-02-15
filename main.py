from Mysql_connector import MysqlConnector, data_mysql
from Rooms import RoomDB, RoomConverter
from Students import StudentDB
from FileReader import JSONReader
from DataExporter import DataExporter


def main():
    room_db = RoomDB(MysqlConnector, data_mysql)
    student_db = StudentDB(MysqlConnector, data_mysql)
    json_reader = JSONReader()
    rooms = json_reader.get_rooms("./rooms.json")
    room_db.load_in_db(rooms)
    students = json_reader.get_students("./students.json")
    student_db.load_in_db(students)
    all_rooms = room_db.get_all()
    data_exporter = DataExporter()
    data_exporter.export_to(all_rooms, "json", "all_rooms_with_counter")


if __name__ == '__main__':
    main()
